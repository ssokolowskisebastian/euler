# What is the largest prime factor of the number 600851475143?
from timer_utils import timer


@timer  # O(√n)
def solution(n=600_851_475_143):
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor = 3 if factor == 2 else factor + 2

    return n


solution()  # result: 6857 took: 0.000131s
