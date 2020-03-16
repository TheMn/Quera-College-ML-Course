import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open('cdf/dists.npz', 'rb') as file:
    npzfile = np.load(file)
    normal_dist = npzfile['normal_dist']
    binomial_dist = npzfile['binomial_dist']
    poisson_dist = npzfile['posson_dist']


def cdf(sample):
    x = np.sort(sample)
    y = np.arange(1, len(x) + 1) / len(x)
    return x, y


def draw_cdf(x, y):
    plt.figure(figsize=(16, 6))
    plt.subplot(211)
    plt.plot(x, y, '.', linestyle='none')
    plt.title("Cumulative Distribution Function")
    plt.show()


draw_cdf(*cdf(normal_dist))
draw_cdf(*cdf(poisson_dist))
draw_cdf(*cdf(binomial_dist))
