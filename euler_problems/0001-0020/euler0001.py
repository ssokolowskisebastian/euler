# Find the sum of all the multiples of 3 or 5 below 1000
from timer_utils import timer


@timer  # O(1)
def solution(limit=10**3):
    def multiples_sum(k):
        m = (limit - 1) // k
        return k * m * (m + 1) // 2

    return multiples_sum(3) + multiples_sum(5) - multiples_sum(15)


solution()  # result: 233168 took: 0.000005s
