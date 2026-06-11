# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from euler_problems.prime_methods import prime_sieve
from timer_utils import timer


@timer  # O(nloglogn) Prime sieve + exp-based LCM
def solution(n=20):
    result = 1
    primes = prime_sieve(n)
    for prime in primes:
        power = prime
        while power * prime <= n:
            power *= prime
        result *= power
    return result


solution()  # result: 232792560 took: 0.000006s
