from timer_utils import timer

with open("../../euler_files/euler0013") as f:
    numbers = [line.strip() for line in f]


@timer #O(mk)
def solution(lst=numbers, n=10):
    return str(sum(int(x[: n + 1]) for x in lst))[:n]


solution()  # result: 5537376230 took: 0.000013s
