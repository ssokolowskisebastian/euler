# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
from collections import defaultdict

from euler_problems.sieve_methods import prime_sieve
from timer_utils import timer


@timer  # O(p)
def solution(n=10_000):
    groups = defaultdict(list)
    primes = prime_sieve(n)
    for p in primes:
        if p > 1487:
            groups["".join(sorted(str(p)))].append(p)

    for group in groups.values():
        if len(group) >= 3:
            group.sort()
            group_set = set(group)
            for i, a in enumerate(group):
                for b in group[i + 1 :]:
                    if (c := 2 * b - a) in group_set:
                        return f"{a}{b}{c}"

    return None


solution()  # result: 296962999629 took: 0.001710s
