from euler_problems.sieve_methods import prime_sieve
from timer_utils import timer


def is_goldbach(n, primes):
    sq = 2
    step = 6

    while sq < n:
        if n - sq in primes:
            return True
        sq += step
        step += 4

    return False


@timer  # O(N^3/2)
def solution(limit=10_000):
    primes = set(prime_sieve(limit))  # O(n loglog n)
    n = 1
    while True:  # O(n)
        n += 2
        if n not in primes and not is_goldbach(n, primes):  # O(n^1/2)
            return n


solution()  # result: 5777 took: 0.001850s
