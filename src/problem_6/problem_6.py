# Solution to problem 6
#
# https://projecteuler.net/problem=6


def sumsquares():
    s = 0
    for i in range(0, 101):
        s += i**2
    return s


def squaressum():
    s = 0
    for i in range(0, 101):
        s += i
    return s**2

print(abs(sumsquares() - squaressum()))

