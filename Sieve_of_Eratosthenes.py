def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    # print(primes)
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
        #print(primes)
    return [p for p in range(2, limit + 1) if primes[p]]
print(sieve_of_eratosthenes(int(input()))
