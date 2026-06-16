# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If 𝑑𝑛 represents the nth digit of the fractional part, find the value of the following expression.
# 𝑑1×𝑑10×𝑑100×𝑑1000×𝑑10000×𝑑100000×𝑑1000000
from timer_utils import timer


def get_digit(n):
    length = 1
    count = 9
    start = 1
    i = 0

    while n > length * count:

        n -= length * count
        count *= 10
        length += 1
        start *= 10

    number = start + (n - 1) // length
    index = (n - 1) % length
    return int(str(number)[index])


@timer  # (log n)
def solution(n=6):
    res = 1
    power = 1
    for _ in range(n + 1):
        res *= get_digit(power)
        print(res)
        power *= 10
    return res


solution(6)  # result: 210 took: 0.000050s
