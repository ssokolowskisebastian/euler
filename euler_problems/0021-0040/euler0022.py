# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?
from timer_utils import timer

with open("../../euler_files/euler0022") as f:
    sorted_names = sorted(f.read().replace('"', "").split(","))


@timer #O(nlogn)
def solution(names=sorted_names):
    scores = [sum(ord(ch) - ord("A") + 1 for ch in name) for name in names]
    return sum(pos * score for pos, score in enumerate(scores, 1))


solution()  # result: 871198282 took: 0.006321s
