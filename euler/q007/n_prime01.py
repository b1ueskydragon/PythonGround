"""
Problem 7: n th prime
faster than list appending.
"""


def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def solve(n_prime=1, i=1, r=10001):
    while n_prime != r:
        i += 2
        if is_prime(i):
            n_prime += 1
    print(i)


solve()
