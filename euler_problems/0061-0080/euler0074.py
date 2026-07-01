from math import factorial
from itertools import combinations_with_replacement


from timer_utils import timer

f = {str(n): factorial(n) for n in range(10)}
next_cache = {}
len_cache = {}


def dfsum(n):
    return tuple(sorted(str(sum(f[d] for d in n))))


def dfsum_cached(n):
    if n not in next_cache:
        next_cache[n] = dfsum(n)
    return next_cache[n]


def chain_len(n):
    path = []
    pos = {}
    x = n

    while True:
        if x in len_cache:
            length = len_cache[x]
            break

        if x in pos:
            # Cycle found
            cycle_start = pos[x]
            cycle_len = len(path) - cycle_start

            # Every node in the cycle has the same chain length
            for y in path[cycle_start:]:
                len_cache[y] = cycle_len

            length = cycle_len
            path = path[:cycle_start]
            break

        pos[x] = len(path)
        path.append(x)
        x = dfsum_cached(x)

    # Fill in the nodes leading to the cycle/cache
    while path:
        y = path.pop()
        length += 1
        len_cache[y] = length

    return len_cache[n]


def count_numbers(state):
    n = len(state)
    total = factorial(n)

    run = 1
    for i in range(1, n):
        if state[i] == state[i - 1]:
            run += 1
        else:
            total //= factorial(run)
            run = 1
    total //= factorial(run)
    if state[0] != "0":
        return total
    else:
        k = state.count("0")
        for j in range(1, k + 1):
            total -= count_numbers(state[j:])
    return total


@timer
def solution():
    count = 0
    digits = "0123456789"
    for l in range(1, 7):
        for state in combinations_with_replacement(digits, l):
            if chain_len(state) == 60:
                count += count_numbers(state)
    return count


solution()  # result: 402 took: 0.060156s
