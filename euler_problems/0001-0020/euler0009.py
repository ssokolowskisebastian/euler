# Pythagorean triplet for which a + b + c = 1000. Find the product abc.
from timer_utils import timer


@timer  # O(n)
def solution(n=1000):
    for a in range(1, n // 3):
        # a + b + c = n, a^2 + b^2 = c^2, c = n - a - b => b = n(n-2a)/2(n-a)
        numerator = n * (n - 2 * a)
        denominator = 2 * (n - a)

        if numerator % denominator != 0:
            continue

        b = numerator // denominator
        c = n - a - b

        if a < b < c:
            return a * b * c
    return None


solution()  # result: 31875000 took: 0.000060s
