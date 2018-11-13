"""
Problem 7: n th prime
"""


def solve(n=10001):
    # if n == 1: return 2

    primes, i = [3], 5  # pre-set
    while len(primes) < n:  # non determined range
        for p in primes:
            if i % p == 0:  # target / prime
                break
        else:
            primes.append(i)
        i += 2  # only odd-num can be a target
    return primes[-2]


print(solve())
