# How many such routes are there through a 20×20 grid?
from timer_utils import timer


@timer # Combinatorial mathematics using the binomial coefficient formula O(min(r,c))
def solution(r=20, c=20):
    total = 1
    for i in range(1, c + 1):
        total *= r + c + 1 - i
        total //= i
    return total


solution()  # result: 137846528820 took: 0.000013s
