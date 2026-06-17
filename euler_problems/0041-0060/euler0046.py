#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
from euler_problems.sieve_methods import prime_sieve
from timer_utils import timer


def is_goldbach(n, primes):
    #2(k+1)^2 = 2k^2 + 4k + 2 =>
    # step = 4k+2, start = 2 * k =>
    # step = 6 && start = 2,  for k = 1
    start = 2
    step = 6

    while start  < n:
        if n - start in primes:
            return True
        start += step
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
