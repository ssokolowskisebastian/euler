# The cube, 41063625 (345³), can be permuted to produce two other cubes: 56623104 (384³) and 66430125 (405³).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
import math
from collections import defaultdict

from timer_utils import timer


def signature(x):
    counts = [0] * 10
    while x:
        counts[x % 10] += 1
        x //= 10
    return tuple(counts)


@timer
def solution(perm=5):

    digits = 1
    i = 1
    groups = defaultdict(list)
    while True:
        cube = i * i * i
        curr_digits = len(str(cube))

        if curr_digits > digits:
            for cubes in groups.values():
                if len(cubes) == perm:
                    return cubes[0]

            groups.clear()
            digits = curr_digits

        groups[signature(cube)].append(cube)
        i += 1


solution()  # result: 127035954683 took: 0.016839s
