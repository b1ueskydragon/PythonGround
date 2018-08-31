import math

# Positive integers only
digit = lambda k: int(math.log10(k))


def is_palindrome(given):
    backup = given # required ?
    acc = []

    for _ in reversed(range(digit(given) + 1)):
        d = (10 ** digit(given))
        k = given // (10 ** digit(given))
        given -= d * k
        acc.append(k)

    return acc


print(is_palindrome(int(input())))
