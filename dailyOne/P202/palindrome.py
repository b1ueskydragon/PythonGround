import math

# Positive integers only
digit = lambda k: int(math.log10(k))


def is_palindrome(given):
    pivot = math.ceil(digit(given) / 2)
    acc = []

    for i, _ in enumerate(reversed(range(digit(given) + 1))):
        if i == pivot:
            break  # TODO reversed half

        d = (10 ** digit(given))
        k = given // (10 ** digit(given))
        given -= d * k
        acc.append(k)

    return acc


print(is_palindrome(int(input())))
