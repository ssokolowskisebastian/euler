from asyncio import graph
from collections import defaultdict

from timer_utils import timer


def poly(s, n):
    return n * ((s - 2) * n - (s - 4)) // 2


def get_poly(s):
    arr = []
    n = 1
    while True:
        x = poly(s, n)
        if x >= 10000:
            break
        if x >= 1000 and x % 100 >= 10:
            arr.append(x)
        n += 1
    return arr


def get_poly_nums():
    return [(s, n) for s in range(3, 9) for n in get_poly(s)]


def is_cyclical(a, b):
    return a % 100 == b // 100


def build_graph(poly_nums):
    graph = defaultdict(list)

    for s, n in poly_nums:
        graph[n // 100].append((s, n))
    return graph


def dfs(gr, path, used):
    if len(path) == 6:
        first = path[0][1]
        last = path[-1][1]
        if is_cyclical(last, first):
            return path

    for poly_type, poly_value in gr[path[-1][1] % 100]:
        if poly_type not in used:
            ans = dfs(gr, path + [(poly_type, poly_value)], used | {poly_type})
            if ans:
                return ans
    return None


@timer
def solution():
    poly = get_poly_nums()
    gr = build_graph(poly)
    for poly_type, poly_value in poly:
        ans = dfs(gr, [(poly_type, poly_value)], {poly_type})
        if ans:
            return sum(x[1] for x in ans)
    return None


solution()  # result: 28684 took: 0.002741s
