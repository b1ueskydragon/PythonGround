import math


def is_palindrome(given):
    # TODO Pythagoras
    # String(x) List(o) ?
    return False


# print(is_palindrome(int(input())))

# Positive integers only
digit = lambda k: int(math.log10(k))

given = 12321

print(given)
print(10 ** digit(given))

given = given - (10 ** digit(given))
print(given)
print(10 ** digit(given))
given = given - (10 ** digit(given))

print(given)
