# If p is the perimeter of a right angle triangle with integral length sides, 𝑎,𝑏,𝑐,
# there are exactly three solutions for 𝑝=120; 20,48,52, 24,45,51, 30,40,50
#
# For which value of 𝑝≤1000, is the number of solutions maximised?
from math import gcd

from timer_utils import timer


@timer  # O(n log n)
def solution(limit=1000):
    count = [0] * (limit + 1)
    max_m = int((limit // 2) ** 0.5)
    for m in range(2, max_m + 1):  # m(m+1) < limit
        for n in range(1, m):
            if (m - n) % 2 == 0:  # one even, one odd (ensures primitive structure)
                continue
            if gcd(m, n) != 1:  # remove scaling option
                continue
            p = 2 * m * (m + n)
            if p > limit:
                continue
            for k in range(p, limit + 1, p):
                count[k] += 1
    return count.index(max(count))


solution()  # result: 840 took: 0.000396s
