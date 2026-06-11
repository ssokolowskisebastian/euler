from timer_utils import timer

with open("../../euler_files/euler0018") as f:
    matrix = [list(map(int, line.split())) for line in f]


@timer  # Dynamic Programming O(n^2)
def solution(mtx=matrix):
    for i in range(len(mtx) - 2, -1, -1):
        for j in range(len(mtx[i])):
            mtx[i][j] += max(mtx[i + 1][j], mtx[i + 1][j + 1])
    return mtx[0][0]


solution()  # result: 1074 took: 0.000054s
