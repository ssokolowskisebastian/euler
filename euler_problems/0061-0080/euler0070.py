from euler_problems.sieve_methods import signature, prime_sieve_range
from timer_utils import timer


@timer
def solution(limit=10_000_000):
    best_n = 0
    best_ratio = float("inf")
    root = int(limit**0.5)

    primes = prime_sieve_range(int(0.7 * root), int(1.3 * root))

    for i, p in enumerate(primes):
        for j in range(i, len(primes) - 1):
            q = primes[j]
            n = p * q

            if n >= limit:
                break

            phi = (p - 1) * (q - 1)

            if n % 9 != phi % 9:
                continue

            if signature(n) != signature(phi):
                continue

            ratio = n / phi

            if ratio < best_ratio:
                best_ratio = ratio
                best_n = n
    return best_n


solution(10_000_000)  # result: 8319823 took: 0.007651s
