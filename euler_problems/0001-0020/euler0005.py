# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from timer_utils import timer


@timer #O(n)
def solution(n=20):
    result = 1
    primes = [2,3,5,7,11,13,17,19]
    for prime in primes:
        power = prime
        while power * prime <= n:
            power *= prime
        result *= power
    return result


solution()  # result: 232792560 took: 0.000006s
