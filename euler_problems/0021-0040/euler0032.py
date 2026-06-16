# 5-digit number, 15234, is 1 through 5 pandigital.
#
# 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
from itertools import permutations

from timer_utils import timer


def is_pandigital(a, b, c):
    s = f"{a}{b}{c}"
    return len(s) == 9 and set(s) == set("123456789")


@timer  # Constrained brute-force
def solution():
    products = set()
    for a in range(2, 10):
        for b in range(1234, 10000 // a):
            p = a * b
            if is_pandigital(a, b, p):
                products.add(p)

    for a in range(12, 99):
        for b in range(123, 10000 // a):
            p = a * b

            if is_pandigital(a, b, p):
                products.add(p)

    return sum(products)


solution()  # result: 45228 took: 0.053769s
