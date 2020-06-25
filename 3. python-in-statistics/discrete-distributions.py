from math import factorial


def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def bern_sim(n, p):
    if p > 1 or p < 0 or n < 1 or not isinstance(n, int):
        return -1
    return p
