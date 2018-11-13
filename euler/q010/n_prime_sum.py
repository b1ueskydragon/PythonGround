"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

below = 2_000_000


def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def solve(r=below, cache=2):
    for i in range(3, r + 1, 2):
        if is_prime(i):
            cache += i
    print(cache)


solve()
