"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

below = 2_000_000


def solve(n=below, cache=0):
    if n < 2:
        return 0
    if n == 2:
        return 2

    n = n + 1 if n % 2 == 0 else n + 2

    primes = [True] * n
    primes[0], primes[1] = None, None  # sentinels

    for i, prime in enumerate(primes):
        if not prime:
            continue  # skip
        elif prime and i <= n ** 0.5 + 1:
            """ eratosthenes' sieve """
            primes[i * 2::i] = [False] * (((n - 1) // i) - 1)

        cache += i

    return cache


print(solve())
