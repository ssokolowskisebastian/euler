import math
from math import isqrt

from timer_utils import timer


@timer
def solution(n):
    scale = 10**200
    res = 0

    for i in range(1, n + 1):
        if isqrt(i) ** 2 == i:
            continue
        root = math.isqrt(i * scale)
        digit = str(root)[:n]
        res += sum(map(int, digit))
    return res


solution(100)  # result: 40886 took: 0.000960s
