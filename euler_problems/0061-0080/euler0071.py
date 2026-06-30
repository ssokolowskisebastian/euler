# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
# find the numerator of the fraction immediately to the left of 3/7.

from timer_utils import timer


@timer
def solution(n=1_000_000):
    d = n - (n - 5) % 7  # 3d - 7n mod 7 = 1 => d = 5x
    return (3 * d - 1) // 7


solution(1_000_000)  # result: 428570 took: 0.000004s
