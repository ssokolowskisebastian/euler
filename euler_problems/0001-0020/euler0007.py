# What is the 10001st prime number?
import math

from euler_problems.prime_methods import prime_sieve
from timer_utils import timer


@timer #O(nloglogn)
def solution(n = 10_000):
    limit = int(n * (math.log(n) + math.log(math.log(n)))) # estimate for the n-th prime.
    return prime_sieve(limit)[n]


solution()  # result: 104743 took: 0.005897s
