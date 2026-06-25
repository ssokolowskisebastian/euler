from timer_utils import timer


@timer  # O(n^2)
def solution(limit=1000):
    n, d = 1, 1
    digits_n = 1
    digits_d = 1
    pow10_n = 10
    pow10_d = 10

    count = 0

    for _ in range(1, limit + 1):
        n, d = n + 2 * d, n + d

        if n >= pow10_n:
            digits_n += 1
            pow10_n *= 10

        if d >= pow10_d:
            digits_d += 1
            pow10_d *= 10

        if digits_n > digits_d:
            count += 1

    return count


solution()  # result: 153 took: 0.000412s
