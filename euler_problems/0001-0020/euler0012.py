# What is the value of the first triangle number to have over five hundred divisors?
from timer_utils import timer


def count_divisors(n):  # O(n^0.5)
    total = 1
    c = 2
    while c * c <= n:
        exp = 0
        while n % c == 0:
            n //= c
            exp += 1
        total *= exp + 1
        c += 1

    if n > 1:
        total *= 2
    return total


def triangle(n):
    return n * (n + 1) // 2


@timer  # O(n^3/2)
def solution(limit=500):
    n = 1
    while True:
        a, b = n, n + 1
        if n % 2 == 0:
            a //= 2
        else:
            b //= 2
        if count_divisors(a) * count_divisors(b) > limit:
            return triangle(n)
        n += 1


solution()  # result: 76576500 took: 0.081027s
