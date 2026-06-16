# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
from euler_problems.sieve_methods import is_prime
from timer_utils import timer


def left_truncatable(prime):
    s = str(prime)
    return all(is_prime(int(s[i:])) for i in range(len(s)))


@timer
def solution():
    total = 0

    def dfs(n):
        nonlocal total
        if n > 10 and left_truncatable(n):
            total += n

        for d in (1, 3, 7, 9):
            m = 10 * n + d

            if is_prime(m):
                dfs(m)

    for p in (2, 3, 5, 7):
        dfs(p)

    return total


solution()  # result: 748317 took: 0.014875s
