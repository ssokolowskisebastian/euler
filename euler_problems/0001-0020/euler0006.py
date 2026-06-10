# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
from timer_utils import timer


@timer #O(1)
def solution(n=100):
    sum_n = n * (n + 1) // 2
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    return sum_n**2 - sum_sq


solution()  # result: 25164150 took: 0.000004s
