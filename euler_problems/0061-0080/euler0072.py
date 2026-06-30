# How many elements would be contained in the set of reduced proper fractions for d<= 1_000_000?
from timer_utils import timer


@timer
def solution(limit):
    phi = list(range(limit + 1))
    for n in range(2, limit + 1, 2):
        phi[n] //= 2

    for p in range(3, limit + 1, 2):
        if phi[p] == p:  # prime
            for k in range(p, limit + 1, p):
                phi[k] -= phi[k] // p

    return sum(phi) - 1


solution(1_000_000)  # result: 303963552391 took: 0.957250s
