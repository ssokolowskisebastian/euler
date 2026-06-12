# Evaluate the sum of all the amicable numbers under 10000.
# The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71, and 142; so d(284) = 220.
# Amicable if d(a) = b and d(b) = a
from euler_problems.prime_methods import divisor_sums
from timer_utils import timer


@timer  # O(nlogn)
def solution(limit=10_000):
    ds = divisor_sums(limit)
    return sum(i for i, s in enumerate(ds) if s < limit and s != i and ds[s] == i)


solution()  # result: 31626 took: 0.008903s
