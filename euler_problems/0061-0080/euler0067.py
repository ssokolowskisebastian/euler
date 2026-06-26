from timer_utils import timer

triangle = open("../../euler_files/euler0067").read()
t = [[int(x) for x in row.split()] for row in triangle.splitlines()]


@timer  # 0(n^2)
def solution():
    for i in range(len(t) - 2, -1, -1):
        for j in range(i + 1):
            a = t[i + 1][j]
            b = t[i + 1][j + 1]
            t[i][j] += a if a > b else b
    return t[0][0]


solution()  # result: 7273 took: 0.000744s
