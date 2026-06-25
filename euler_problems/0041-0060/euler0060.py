# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from euler_problems.sieve_methods import prime_sieve, miller_rabin
from timer_utils import timer

pair_cache = {}
pow10 = {}


def concat(a, b):

    digits = len(str(b))

    if digits not in pow10:
        pow10[digits] = 10**digits

    return a * pow10[digits] + b


def connected(a, b):
    key = (a, b) if a < b else (b, a)

    if key not in pair_cache:
        pair_cache[key] = miller_rabin(concat(a, b)) and miller_rabin(concat(b, a))

    return pair_cache[key]


def search(primes, target=5, last_prime=3, clique=[]):
    if len(clique) == target:
        return clique

    for p in primes:
        if p <= last_prime:
            continue
        if all(connected(p, q) for q in clique):
            if result := search(
                primes,
                target,
                p,
                clique + [p],
            ):
                return result
    return None


@timer
def solution(limit=10_000):

    return search(prime_sieve(limit))


solution()  # result: 26033 took: 0.442771s
