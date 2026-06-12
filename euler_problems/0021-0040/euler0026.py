# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from euler_problems.sieve_methods import prime_sieve, divisors
from timer_utils import timer


def cycle_len(p):
    for d in divisors(p - 1):  # O(p^0.5)
        if pow(10, d, p) == 1:  # O(logp)
            print(p, d)
            return d
    return None


@timer  # O(n^3/2)
def solution(n=1000):
    max_len, num = 0, 0
    primes = prime_sieve(n)[3:]  # O(n log log n)
    for p in primes:
        length = cycle_len(p)
        if max_len < length:
            max_len, num = length, p
    return num


solution()  # result: 983 took: 0.007859s
