# Fibonacci sequence whose values do not exceed 4_000_000, find the sum of the even-valued terms.

from timer_utils import timer


@timer  # O(log n)
def solution(n=4_000_000):
    previous, current = 2, 8
    total = previous
    while current < n:
        total += current
        previous, current = current, previous + 4 * current

    return total

solution()  # result: 4613732 took: 0.000005s
