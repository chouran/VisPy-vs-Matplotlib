import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from vispy import app

# Parameters

nb_point = [100, 1000, 10000, 100000, 100000000]
nb_signal = 10
memory_plt = []


def data(N, n):
    """"
    N = total nb of points
    n = number of signal
    """
    n_samples = int(N/n)
    noise = np.random.normal(0, 1, n_samples)
    x = np.linspace(0, nb_point)
    y = np.random.rand(nb_signal, n_points)
