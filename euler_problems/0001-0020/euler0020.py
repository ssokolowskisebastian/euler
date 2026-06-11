# Find the sum of the digits in the number 100!
from math import factorial

from timer_utils import timer


@timer #O(nlogn) divide-and-conquer
def solution(n=100):
    return sum(map(int,str(factorial(n))))


solution()  # result: 648 took: 0.000031s
