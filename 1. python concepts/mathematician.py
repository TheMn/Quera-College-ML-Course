import math


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def dif(x, y):
    return x / y


def pow(x, y):
    return x ** y


def gcd(x, y):
    return math.gcd(x, y)


def log(x, y):
    return math.log(x, y)


while True:
    inp = input()
    if inp == "end":
        break
    exec(inp)
