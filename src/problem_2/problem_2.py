# Solution to problem 2
#
# https://projecteuler.net/problem=2


def fibonacci():
    limit = 4000000
    a = 1
    b = 2
    s = 0

    while b < limit:
        if b % 2 == 0:
            s += b
        c = a + b
        a = b
        b = c

    return s

print(fibonacci())

