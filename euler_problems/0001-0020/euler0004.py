# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers
from timer_utils import timer


def make_palindrome(i):
    s = str(i)
    return int(s + s[::-1])


def is_valid(pal, lower, upper):
    for d in range(upper, lower, -1):
        if pal % d == 0:
            q = pal // d
            if lower < q <= upper:
                return True
        if d * d < pal:
            break
    return False


@timer  # ~O(10^2*n) optimized brute force
def solution(n=3):
    upper = 10**n - 1
    lower = 10 ** (n - 1) - 1
    for i in range(upper, lower, -1):
        pal = make_palindrome(i)
        if is_valid(pal, lower, upper):
            return pal
    return None


solution()  # result: 906609 took: 0.000330s
