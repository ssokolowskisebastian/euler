# Find the value of D <=7  in minimal solutions of  for which the largest value of  is obtained.
from math import isqrt

from timer_utils import timer


def pell(D):
    a0 = isqrt(D)
    m, d, a = 0, 1, a0

    p1, p0 = a, 1
    q1, q0 = 1, 0

    while True:

        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d

        p0, p1 = (
            p1,
            a * p1 + p0,
        )
        q0, q1 = (
            q1,
            a * q1 + q0,
        )

        if p1 * p1 - D * q1 * q1 == 1:
            return p1


@timer  # 0(n^3/2) iterative recurrence approach
def solution(limit=1000):
    best_n = 0
    best_d = 0

    sq = 2
    nxt_sq = 4

    for d in range(2, limit):
        if nxt_sq == d:
            sq += 1
            nxt_sq = sq * sq
            continue

        x = pell(d)

        if x > best_n:
            best_d = d
            best_n = x
    return best_d


solution()  # result: 661 took: 0.006937s
