# Solution to problem 1
#
# https://projecteuler.net/problem=1


def run():
    s = 0
    for x in range(0, 1000):
        if x % 3 == 0 or x % 5 == 0:
            s += x
    return s

print(run())