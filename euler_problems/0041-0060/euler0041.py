# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
from itertools import permutations

from euler_problems.sieve_methods import is_prime
from timer_utils import timer


@timer  # descending permutation
def solution():
    digits = "7654321"
    for p in permutations(digits):
        if p[-1] not in "137":
            continue

        n = int("".join(p))

        if is_prime(n):
            return n
    return None


solution()  # result: 7652413 took: 0.000270s
