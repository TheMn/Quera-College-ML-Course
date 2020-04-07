def bern_sim(n, p):
    if p > 1 or p < 0 or n < 1 or not isinstance(n, int):
        return -1
    return p

# succ = 0
# for k in range(n + 1):
#     succ += comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
