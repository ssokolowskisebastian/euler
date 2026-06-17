from timer_utils import timer


def is_pentagonal(x):  # O(1)
    d = 24 * x + 1
    r = int(d**0.5)
    return r * r == d and (1 + r) % 6 == 0


@timer
def solution():  # O(k)
    k = 144
    while True:
        if is_pentagonal(k * (2 * k - 1)):
            return k * (2 * k - 1)
        k += 1


solution()  # result: 1533776805 took: 0.018701s
