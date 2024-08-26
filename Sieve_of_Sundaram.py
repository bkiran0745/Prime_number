def sieve_of_sundaram(limit):
    k = (limit - 1) // 2
    integers = [True] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            integers[i + j + 2 * i * j] = False
            j += 1
    if limit > 2:
        primes = [2] + [2 * i + 1 for i in range(1, k + 1) if integers[i]]
    else:
        primes = []
    return primes
print(sieve_of_sundaram(int(input())))