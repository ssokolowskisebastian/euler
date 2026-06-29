from euler_problems.sieve_methods import prime
from timer_utils import timer


@timer
def solution(n):
    primes = prime()
    res = 1
    for p in primes:
        if res * p > n:
            break
        res *= p

    return res


solution(1_000_000)  # result: 510510 took: 0.000016s
