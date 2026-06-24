# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.
from collections import defaultdict
from itertools import combinations

from euler_problems.sieve_methods import prime_sieve
from timer_utils import timer


@timer  # O(n log n)
def solution(limit=1_000_000):
    primes = prime_sieve(limit)
    prime_set = set(primes)
    digits = "0123456789"

    for prime in primes:
        if prime < 100_000:
            continue
        str_prime = str(prime)

        for s in set(str_prime):
            if str_prime.count(s) < 3:
                continue

            count = 0
            fail = 0

            for digit in digits:
                candidate = str_prime.replace(s, digit)

                if candidate[0] == "0":
                    fail += 1
                elif int(candidate) in prime_set:
                    count += 1
                else:
                    fail += 1

                if fail > 2:
                    break

            if count == 8:
                return prime
    return None


solution()  # result: 121313 took: 0.074264s
