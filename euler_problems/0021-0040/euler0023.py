# A number n is called deficient if the sum of its proper divisors is less than n
# It is called abundant if this sum exceeds n.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from euler_problems.sieve_methods import divisor_sums
from timer_utils import timer


@timer
def solution(limit=28123):
    div_sums = divisor_sums(limit)
    abundant_lst = [i for i in range(12, limit + 1) if div_sums[i] > i]  # O(nlogn)
    n = len(abundant_lst)
    can = [0] * (limit + 1)

    for i in range(n):  # O(A^2)
        a = abundant_lst[i]
        for j in range(i, n):
            s = a + abundant_lst[j]
            if s > limit:
                break

            can[s] = 1
    return sum(i for i in range(1, limit + 1) if can[i] == 0)


solution()  # result: 4179871 took: 1.322757s
