# Solution to problem 3
#
# https://projecteuler.net/problem=3


def compute():
    n = 600851475143
    factor = 2
    lastfactor = 0
    while n > 1:
        if n % factor == 0:
            lastfactor = factor
            n /= factor
            while n % factor == 0:
                n /= factor
        factor += 1
    return lastfactor

print(compute())
