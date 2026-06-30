from euler_problems.sieve_methods import prime_sieve
from timer_utils import timer


def num_ways(limit):
    ways = [0] * (limit + 1)
    ways[0] = 1
    primes = prime_sieve(limit)

    for p in primes:
        for i in range(p, limit + 1):
            ways[i] += ways[i - p]

    return ways


@timer
def solution(limit, target):
    for i, x in enumerate(num_ways(limit)):
        if x > target:
            return i
    return None


solution(100, 5000)
