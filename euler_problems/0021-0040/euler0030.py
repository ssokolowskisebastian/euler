# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
from itertools import combinations_with_replacement

from timer_utils import timer


def add_arrays(a, b):
    return [0] * (len(a) - len(b)) + b


@timer
def solution(power=5):
    dp = [d**power for d in range(10)]
    max_digits = 1
    while 10**max_digits <= max_digits * dp[-1]:
        max_digits += 1

    total = 0

    for digits in combinations_with_replacement(range(10), max_digits):
        s = sum(dp[d] for d in digits)
        a = sorted(map(int, str(s)))
        if sorted(digits) == [0] * (len(digits) - len(a)) + a:
            total += s
    return total - 1


solution()  # result: 443839 took: 0.016322s
