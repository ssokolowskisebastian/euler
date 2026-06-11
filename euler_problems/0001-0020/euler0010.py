# Find the sum of all the primes below two million.
from euler_problems.prime_methods import prime_sieve
from timer_utils import timer


@timer #time complexity: O(nloglogn)
def solution(n=2_000_000):
    return sum(prime_sieve(n))


solution()  # result: 142913828922 took: 0.249826s
