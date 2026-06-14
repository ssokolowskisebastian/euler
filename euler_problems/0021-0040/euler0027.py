# The incredible formula 𝑛2−79𝑛+1601 was discovered, which produces 80 primes for the consecutive values 0<𝑛<79
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form 𝑛^2+𝑎𝑛+𝑏,
# where |𝑎|<1000 and |𝑏|<1000 where |𝑛| is the modulus/absolute value of 𝑛.
# Find the product of the coefficients, 𝑎 and 𝑏
# for the quadratic expression that produces the maximum number of primes for consecutive values of 𝑛
# starting with 𝑛=0.
from euler_problems.sieve_methods import prime_sieve, is_prime
from timer_utils import timer


def length_consecutive(a: int, b: int) -> int:  # O(L)
    k = 2
    while True:
        val = k * k + a * k + b
        if not is_prime(val):
            break
        k += 1
    return k


@timer
def solution(n=1000):  # O(n^4) Brute force
    a_best, b_best, max_length = 0, 0, 0
    b_possible = prime_sieve(n)  # n = 0 => b is prime

    for b in b_possible:  # O(nloglogn)
        for a in range(-n + 1, -1):  # O(n)
            if not is_prime(a + b + 1):  # n = 1 => a + b + 1  is prime #O(n^0.5)
                continue
            length = length_consecutive(a, b)  # O(L)
            if length > max_length:
                max_length = length
                a_best = a
                b_best = b

    return a_best * b_best


solution(1000)  # result: -59231 took: 0.091004s
