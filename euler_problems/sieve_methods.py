from random import randint, randrange


def is_prime(n):  # O(n^0.5)
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_sieve(n):  # O(n log log n)
    sieve = [True] * ((n + 1) // 2)
    sieve[0] = [False]
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if sieve[i // 2]:
            start = i * i // 2
            sieve[start::i] = [False] * len(sieve[start::i])
    primes = [2]
    for k in range(1, len(sieve)):
        if sieve[k]:
            p = 2 * k + 1
            if p < n:
                primes.append(p)

    return primes


def divisor_sums(limit):  # (nlogn) n times harmonic sum
    div_sum = [0] * (limit + 1)
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            div_sum[j] += i
    return div_sum


def divisors(n):  # O(n^0.5)
    factors = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            factors.append(d)
            if d * d != n:
                factors.append(n // d)

    return sorted(factors)


small_primes = set(prime_sieve(100))


def is_divisible_by_small_prime(n: int) -> bool:

    return any(n % p == 0 for p in small_primes)


def witness(a, s, d, n):
    x = pow(a, d, n)

    for _ in range(s):
        if x == n - 1:
            return True

        x = (x * x) % n

    return x == 1


def miller_rabin(n):
    if n in small_primes:
        return True
    if is_divisible_by_small_prime(n):
        return False

    d, s = n - 1, 0  # a^n-1 mod n = 1 if n is prime Fermat's Little Theorem
    while d % 2 == 0:
        d //= 2  # a^d, a^2d,, a^4d, ...
        s += 1

    a = randrange(2, n - 2)

    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    for _ in range(s - 1):
        x = (x * x) % n

        if x == n - 1:
            return True

    return False
