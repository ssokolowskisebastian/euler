# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
from itertools import combinations_with_replacement
from math import factorial

from timer_utils import timer


@timer  # Combinatorical
def solution():
    fact = [factorial(i) for i in range(10)]
    total = 0
    for length in range(2, 8):
        for digits in combinations_with_replacement(range(10), length):
            s = sum(fact[d] for d in digits)
            ds = sorted(map(int, str(s)))

            if list(digits) == ds:
                total += s

    return total


solution()  # result: 40730 took: 3.493988s
