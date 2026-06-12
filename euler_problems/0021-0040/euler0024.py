# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
from math import factorial

from timer_utils import timer


@timer #O(d^2)
def solution(d=10, n=10**6 - 1):
    digits = list(map(str, range(d)))
    result = ""
    for i in range(d - 1, -1, -1): #O(d)
        fact = factorial(i)
        index = n // fact
        result += digits.pop(index) #O(d)
        n %= fact
    return result


solution()  # result: 2783915460 took: 0.000066s
