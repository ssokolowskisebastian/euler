from math import gcd, isqrt


from timer_utils import timer


@timer
def solution(limit):
    cnt = [0] * (limit + 1)
    m_max = (isqrt(2 * limit - 1) - 1) // 2  # p = 2m(m+n)
    for m in range(2, m_max + 1):
        for n in range(m - 1, 0, -2):
            if gcd(m, n) == 1:
                p = 2 * m * (m + n)
                for k in range(p, limit + 1, p):
                    cnt[k] += 1
        m += 1

    return cnt.count(1)


solution(1_500_000)  # result: 161667 took: 0.413834s
