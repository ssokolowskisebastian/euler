import sys

from timer_utils import timer


@timer  # O(n logn)
def solution(a=1, b=3, c=1, d=2, limit=12_000):
    range_counters = [0] * (limit + 1)
    used = [0] * (limit + 1)
    result = 0

    for q in range(2, limit + 1):
        r1 = (a * q) // b + 1
        r2 = (c * q - 1) // d
        if r2 >= r1:
            range_counters[q] = r2 - r1 + 1

    for i in range(2, limit + 1):
        count = range_counters[i]
        if count == 0:
            continue

        rem = count - used[i]
        if rem > 0:
            result += rem
            for j in range(2 * i, limit + 1, i):
                used[j] += rem

    return result


solution()  # result: 7295372 took: 0.018486s
