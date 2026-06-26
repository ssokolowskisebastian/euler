import itertools
import math

from timer_utils import timer


@timer
def solution():
    total = 0
    n = 1
    while True:
        x = 10 ** ((n - 1) / n)
        count = 9 - int(x) + (x == int(x))
        if count <= 0:
            return total
        total += count
        n += 1


solution()  # result: 49 took: 0.000022s
