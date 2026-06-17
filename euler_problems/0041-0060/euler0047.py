# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23 645 = 3 × 5 × 43 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?
from timer_utils import timer


@timer  # O(N log logN)
def solution(limit, k=4):
    streak = 0
    count = [0] * (limit + 1)
    for i in range(2, limit):
        if count[i] == 0:
            for j in range(i, limit, i):
                count[j] += 1
        streak = streak + 1 if count[i] == k else 0
        if streak == k:
            return i - k + 1
    return None


solution(140_000)  # result: 134043 took: 0.043494s
