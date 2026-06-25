# A googol (10^100) is a massive number: one followed by one-hundred zeros;
#
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, 𝑎𝑏, where 𝑎,𝑏<100, what is the maximum digital sum?
from timer_utils import timer


@timer
def solution(limit=100):
    max_digits = 0
    for a in range(limit - 10, limit):
        num = a ** (limit - 10)
        for _ in range(limit - 9, limit):
            max_digits = max(sum(map(int, str(num))), max_digits)
            num *= a
    return max_digits


solution()  # result: 972 took: 0.001481s
