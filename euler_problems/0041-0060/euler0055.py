# f we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
# . In addition you are given that for every number below ten-thousand, it will either
# (i) become a palindrome in less than fifty iterations, or,
# (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
# In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664
# (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
from timer_utils import timer


def reverse(n):  # log n
    r = 0
    while n:
        r = r * 10 + n % 10
        n //= 10
    return r


def is_lychel(n, max_iter=50):  # O(max_iter)
    for _ in range(max_iter):
        n += reverse(n)
        if n == reverse(n):
            return False
    return True


@timer  # O(max_iter * n log n)
def solution(limit=10_000):
    return sum(1 for n in range(1, limit) if is_lychel(n))


solution()  # result: 249 took: 0.157725s
