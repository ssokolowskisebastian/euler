# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits
from timer_utils import timer


def signature(n):
    counts = [0] * 10
    while n:
        counts[n % 10] += 1
        n //= 10
    return counts


@timer  # (10^d / 135) Brute Force with Number Pruning
def solution():
    d = 1

    while True:
        start = 10 ** (d - 1) + 8  # mod(start, 9) == 0
        end = 10**d // 6
        for x in range(start, end, 9):
            s = signature(x)
            if all(signature(k * x) == s for k in range(2, 7)):
                return x

        d += 1


solution()  # result: 142857 took: 0.014046s
