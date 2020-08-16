import numpy as np
import matplotlib.pyplot as plt

nb_points = [100, 1000, 10000, 100000, 1000000, 10000000, 50000000]
mem_plt = [80.4, 85.6, 97.41, 201.12, 883.95, 1250.95, 3364.89]
mem_vsp = [75.78, 77.38, 83.26, 85.6, 125.30, 557.21, 2476.73]
ffr_plt = [0.63, 0.67, 1.06, 8.1, 46, 64.71, 71.39]
ffr_vsp = [0.42, 0.47, 0.57, 0.60, 1.05, 4.56, 13.83]

fig, ax = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.3)
ax[0].plot(nb_points, mem_plt, marker='o', color='b')
ax[0].plot(nb_points, mem_vsp, marker='x', color='g')
ax[0].set_xscale('log')
ax[0].set_xlabel('Number of points')
ax[0].set_ylabel('Memory (MB)')
ax[0].set_title('A')
ax[0].grid(True)

ax[1].plot(nb_points, ffr_plt, marker='o', color='b')
ax[1].plot(nb_points, ffr_vsp, marker='x', color='g')
ax[1].set_xscale('log')
ax[1].set_xlabel('Number of points')
ax[1].set_ylabel('First Frame Rendering(s)')
ax[1].set_title('B')
ax[1].grid(True)
plt.legend(('Matplotlib', 'VisPy'), loc='upper left')
plt.show()
