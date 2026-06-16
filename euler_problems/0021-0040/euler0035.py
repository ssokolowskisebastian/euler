# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
from euler_problems.sieve_methods import prime_sieve
from timer_utils import timer


def cycle(n):
    digits = str(n)

    for _ in range(len(digits)):
        yield int(digits)
        digits = digits[1:] + digits[0]


@timer  # sieve O(n log log n)
def solution(n=1_000_000):

    primes = set(prime_sieve(n))
    seen = {2, 3, 5, 7}
    bad = set("024568")

    for prime in primes:
        if prime in seen:
            continue
        if any(ch in bad for ch in str(prime)):
            continue

        rotations = list(cycle(prime))

        if all(r in primes for r in rotations):
            seen.update(rotations)
    return len(seen)


solution()  # result: 55 took: 0.121789s
