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