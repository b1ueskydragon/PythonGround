"""
Given n numbers, find the greatest common denominator between them.
"""


def find_gcd(given):
    """
    O(k*N)
    k = a size of head element of given list
    N = an length of given list
    """

    return 1


def is_prime(num):
    if num < 2 or (num is not 2 and num % 2 is 0):
        return False
    for _ in range(3, num, 2):
        if num % _ is 0:
            return False
        else:
            continue
    return True


def primes(num):
    return [i for i in reversed(range(num + 1)) if is_prime(i)]

print(primes(42))

# isPrime ? (return 1 if, all of elements are prime)
# primes ? (else, division with primes continuously)

given = [42, 56, 14]
print(find_gcd(given))
