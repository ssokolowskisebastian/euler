# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
from timer_utils import timer

"""For layer k, the top-right corner is: (2k+1)^2 others:(2k+1)^2-2k, (2k+1)^2-4k, (2k+1)^2-6k Sk = 16k^2+4k+4"""
"""result = 1 + sum(16k^2+4k+4 for k in range(1, (n-1)//2 +1)"""


@timer  # O(1)
def solution(n):
    m = (n - 1) // 2
    sum_k = m * (m + 1) // 2
    sum_k2 = m * (m + 1) * (2 * m + 1) // 6

    return 1 + 16 * sum_k2 + 4 * sum_k + 4 * m


solution(1001)  # result: 669171001 took: 0.000005s
