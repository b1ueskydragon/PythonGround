"""
Problem 7: 10001 th prime

Eratosthenes' sieve.
"""

target = 10_001
expected = 105_000  # bigger than given


def solve(n=target, size=expected):
    # pre-cached
    primes = [True] * size

    # sentinels (0 and 1 is not prime)
    primes[0], primes[1] = False, False

    count = 0
    for i, prime in enumerate(primes):
        if prime:
            count += 1
            """ 
            set `i`(i*1) to True, 
            then set all multiples of `i` (i*2, i*3, ...) to False.
            """
            # (((size - 1) // i) - 1) == len(primes[i * 2::i])
            primes[i * 2::i] = [False] * (((size - 1) // i) - 1)

        # if primes[i] is True, `i` is prime.
        if count == n:
            return i


print(solve())
