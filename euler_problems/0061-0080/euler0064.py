from math import isqrt


from timer_utils import timer


def period_length(n):
    a0 = isqrt(n)
    period = 0
    if a0 * a0 == n:
        return period

    m, d, a = 0, 1, a0

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1

        if a == 2 * a0:
            return period


@timer  # O(n^3/2)
def solution(n=10_000):
    return sum(1 for i in range(n) if period_length(i) % 2)


solution()  # result: 1322 took: 0.056745s
