from timer_utils import timer

with open("../../euler_files/euler0011") as f:
    grid = "".join(line for line in f)

matrix = [list(map(int, x.split())) for x in grid.strip().split("\n")]


@timer  # Brute Force Approach
def solution(matrix=matrix, l=4):
    row, col = len(matrix), len(matrix[0])
    max_product = 1
    # down
    for i in range(row - l + 1):
        for j in range(col):
            total = 1
            for x in range(l):
                total *= matrix[i + x][j]
            if total > max_product:
                max_product = total
    # left
    for i in range(row):
        for j in range(col - l + 1):
            total = 1
            for x in range(l):
                total *= matrix[i][j + x]
            if total > max_product:
                max_product = total
    # diag down left
    for i in range(row - l + 1):
        for j in range(col - l + 1):
            total = 1
            for x in range(l):
                total *= matrix[i + x][j + x]
            if total > max_product:
                max_product = total
    # diag up right
    for i in range(l, row):
        for j in range(col - l + 1):
            total = 1
            for x in range(l):
                total *= matrix[i - x][j + x]
            if total > max_product:
                max_product = total

    return max_product


solution()  # result: 70600674 took: 0.000410s
