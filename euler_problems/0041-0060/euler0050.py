# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from euler_problems.sieve_methods import prime_sieve
from timer_utils import timer


@timer
def solution(limit=1_000_000):
    primes = prime_sieve(limit) # O(n log log n)
    prime_set = set(primes)
    prefix = [0]

    for p in primes:
        nxt = prefix[-1] + p
        if nxt > limit:
            break
        prefix.append(nxt)

    offset = 1

    while offset < len(prefix):
        end_sum = prefix[-offset]
        threshold = prefix[-offset - 1]
        for start_sum in prefix:
            candidate = end_sum - start_sum
            if candidate < threshold:
                offset += 1
                break
            if candidate in prime_set:
                return candidate
        else:
            break
    return None


solution()  # result: 997651 took: 0.068793s
