# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even) n → 3n + 1 (n is odd)
# Starting with 13: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Which starting number, under one million, produces the longest chain?
from timer_utils import timer


@timer  # Dynamic Programming O(n)
def solution(limit=1_000_000):
    best_len = 0
    best_n = 1
    cache = {1: 1}

    for i in range(2, limit):
        n = i
        path = []
        while n not in cache:
            path.append(n)
            if n & 1:
                n = 3 * n + 1
            else:
                n >>= 1
        length = cache[n]

        for x in reversed(path):
            length += 1
            cache[x] = length

        if cache[i] > best_len:
            best_len = cache[i]
            best_n = i
    return best_n


solution()  # result: 837799 took: 1.642064s
