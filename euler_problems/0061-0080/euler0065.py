from timer_utils import timer


def e_continued_fraction(n):
    yield 2
    k = 2
    for i in range(1, n):
        flag = i % 3 == 2
        yield k if flag else 1
        k += 2 * flag


@timer  # 0(n^2) dynamic programming approach
def solution(n=100):
    it = e_continued_fraction(n)

    num, prev = next(it), 1

    for a in it:
        num, prev = a * num + prev, num

    return sum(int(c) for c in str(num))


solution()  # result: 272 took: 0.000047s
