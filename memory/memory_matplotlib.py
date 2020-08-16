import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import psutil
from memory_profiler import memory_usage, profile
from vispy import app

#parameters
nb_signals = 10
nb_points = 100
nb_samples = int(nb_points/nb_signals)

#data
x = np.linspace(0, nb_samples, nb_samples)
y = np.random.rand(nb_signals, nb_samples)

@profile
def plot_func(n_signals):
    plt.plot(x, np.transpose(y))
    plt.show()
    return


@profile
def run_plot(n):
    plot_func(n)

plot_func(nb_signals)
