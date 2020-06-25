import math
import numpy as np


def calc(last_days, k):
    lmbda = np.mean(last_days)
    return (math.e ** (-lmbda)) * ((lmbda ** k) / math.factorial(k))
