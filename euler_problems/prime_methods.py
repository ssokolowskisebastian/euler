def prime_sieve(n):
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



