# What is the sum of the digits of the number 2^1000 ?
from timer_utils import timer


@timer  # Brute force O(nlogn)
def solution(n=1000):
    return sum(map(int, str(1 << n)))


solution()  # result: 1366 took: 0.000064s
