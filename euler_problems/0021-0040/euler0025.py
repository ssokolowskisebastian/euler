# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
from math import log10, ceil
from timer_utils import timer


@timer #O(1) Binet's formula
def solution(n=10**3):
    phi = (1 + 5**0.5) / 2
    return ceil((n - 1 + log10(5**0.5)) / log10(phi))


solution()  # result: 4782 took: 0.000007s
