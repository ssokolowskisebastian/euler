# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from math import gcd

from timer_utils import timer


@timer  # brute force
def solution(n=100):
    num = 1
    den = 1

    for d in range(10, n):
        for n in range(10, d):
            n0 = n % 10
            n1 = n // 10
            d0 = d % 10
            d1 = d // 10

            if n1 == d0 and n0 * d == n * d1:
                num *= n
                den *= d
            elif n0 == d1 and n1 * d == n * d0:
                num *= n
                den *= d

    return den // gcd(num, den)


solution()  # result: 100 took: 0.000817s
