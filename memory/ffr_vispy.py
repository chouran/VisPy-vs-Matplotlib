import sys
import numpy as np
import time
from vispy import app, gloo

# Box Shader
BOX_VERT_SHADER = """
attribute vec2 a_position;
void main() {
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""

BOX_FRAG_SHADER = """
// Fragment shader.
void main() {
    gl_FragColor = vec4(1.0, 0.0, 1.0, 1.0);
}
"""

# Signals

SIGNAL_VERT_SHADER = """
attribute float a_values;
attribute vec3 a_colors;
attribute float a_index_x;
attribute float a_index_signal;

uniform vec2 u_scale;
uniform float u_max_value;
uniform float u_nb_samples;

varying vec3 v_colors;
varying float v_index;

void main() {
    float x = -0.9 + (1.8 * (a_index_x / u_nb_samples) * u_scale.x);
    float y = -0.9 + a_values/u_max_value;
    vec2 position = vec2(x, y);   
    gl_Position = vec4(position, 0.0, 1.0);
    v_colors = a_colors;
    v_index = a_index_signal;
}
"""

SIGNAL_FRAG_SHADER = """
varying float v_index;
varying vec3 v_colors;

// Fragment shader.
void main() {
    gl_FragColor = vec4(v_colors, 1.0);
    if (fract(v_index) > 0.0)
            discard;
}
"""

# parameters
nb_signals = 10
nb_points = 50000000
nb_samples = int(nb_points / nb_signals)

# data
x_index = np.tile(np.linspace(0, nb_samples-1, nb_samples), reps=nb_signals).astype(np.float32)
y_values = np.random.rand(nb_signals, nb_samples).astype(np.float32)
signal_index = np.repeat(np.linspace(0, nb_signals-1, nb_signals), repeats=nb_samples).astype(np.float32)
color = np.repeat(np.random.uniform(size=(nb_signals, 3), low=.5, high=.9),
                  nb_samples, axis=0).astype(np.float32)

box_position = np.array([[-0.9, -0.9], [0.9, -0.9], [0.9, 0.9], [-0.9, 0.9],
                        [-0.9, -0.9]], dtype=np.float32)
box_color = np.array([[1.0, 1.0, 1.0]]).astype(np.float32)


class SignalCanvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, title='Use your wheel to zoom!', show=False,
                            keys='interactive')

        # Signal
        self.program = gloo.Program(SIGNAL_VERT_SHADER, SIGNAL_FRAG_SHADER)
        self.program['a_values'] = y_values.reshape(-1, 1)
        self.program['a_colors'] = color
        self.program['a_index_x'] = x_index
        self.program['a_index_signal'] = signal_index
        self.program['u_scale'] = (1., 1.)
        self.program['u_nb_samples'] = nb_samples
        self.program['u_max_value'] = 1.0

        # Box
        self.program_box = gloo.Program(vert=BOX_VERT_SHADER, frag=BOX_FRAG_SHADER)
        self.program_box['a_position'] = box_position

        gloo.set_viewport(0, 0, *self.physical_size)

        #self._timer = app.Timer('auto', connect=self.on_timer, start=True)
        gloo.set_state(clear_color='black', blend=True,
                       blend_func=('src_alpha', 'one_minus_src_alpha'))
        self.show()

    def on_resize(self, event):
        gloo.set_viewport(0, 0, *event.physical_size)

    def on_draw(self, event):
        gloo.clear()
        self.program.draw('line_strip')
        self.program_box.draw('line_strip')


t0 = time.clock()
c = SignalCanvas()
app.run()
t1 = time.clock()
print(t1 - t0)
