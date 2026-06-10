# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers
from timer_utils import timer


@timer #~O(n*10^n)
def solution(n=3):
    upper = 10**n
    lower = 10 ** (n - 1) - 1
    for i in range(upper, lower, -1):
        s = str(i)
        pal = int(s + s[::-1])
        for d in range(upper, lower, -1):
            if d * d < pal:
                break
            if pal % d == 0 and lower < pal // d < upper:
                return pal
    return None


solution()  # result: 906609 took: 0.000330s
