"""
Problem 7: n th prime
"""


def find_prime(n):
    primes, i = [2, 3], 5  # pre-set
    while len(primes) < n:  # non determined range
        for p in primes:
            if i % p == 0:  # target / prime
                break
        else:
            primes += [i]
        i += 2  # only odd-num can be a target
    return primes[-1]


print(find_prime(int(input())))
