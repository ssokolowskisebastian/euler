# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
from math import ceil

from timer_utils import timer


def is_palindromic_base2(n):
    s = str(bin(n)[2:])
    return s == s[::-1]


@timer  # Palindrome generation O(2* 10^n/2)
def solution(n=6):
    total = 0
    upper = 10 ** ((n + 1) // 2)
    limit = 10 ** n
    for i in range(1, upper):
        s = str(i)
        p = int(s + s[-2::-1])
        q = int(s + s[::-1])

        if p < limit and p & 1 and is_palindromic_base2(p):
            total += p
        if q < limit and q & 1 and is_palindromic_base2(q):
            total += q

    return total


solution()  # result: 872187 took: 0.002895s
