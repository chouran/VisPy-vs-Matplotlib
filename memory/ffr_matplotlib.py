import numpy as np
import matplotlib.pyplot as plt
import time
print(plt.get_backend())


#parameters
nb_signals = 10
nb_points = 50000000
nb_samples = int(nb_points/nb_signals)

#data
x = np.linspace(0, nb_samples-1, nb_samples)
y = np.random.rand(nb_signals, nb_samples)
print(x.shape, y.shape, np.transpose(y).shape)

def plot_func(n_signals):
    fig, ax = plt.subplots()
    ax.plot(x, np.transpose(y))
    plt.show()
    plt.close(fig)


t0 = time.clock()
plot_func(nb_signals)
t1 = time.clock()
print(t1-t0)
