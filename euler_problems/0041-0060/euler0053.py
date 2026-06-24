# How many, not necessarily distinct, values of C(n,r) for n <= 100 , are greater than one-million?
from timer_utils import timer


@timer  # O(n^3/2) brute force with combinatorical pruning
def solution(num=100, min_value=10**6):
    total = 0
    for n in range(1, num + 1):
        value = 1
        for r in range(1, n):
            value = value * (n - r + 1) // r  # C(n,r) = C(n,r-1) * (n-r+1)/r
            if value > min_value:
                total += (
                    n - 2 * r + 1
                )  # once exceeds threshold the number of valid pairs is
                break
    return total


solution()  # result: 4075 took: 0.000097s
