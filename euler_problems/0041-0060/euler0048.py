# Find the last ten digits of the series, 1^1+2^2+3^3+…+1000^1000
from timer_utils import timer


@timer  # ∑O(logi) = O(nlogn)
def solution(limit=1000):
    mod = 10**10
    return sum(pow(i, i, mod) for i in range(1, limit + 1)) % mod


solution()  # result: 9110846700 took: 0.002567s
