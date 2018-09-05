import math


def is_palindrome(num):
    if num < 0:
        return False

    rem = num % 10
    num //= 10

    if num is 0:
        return True
    if rem is 0:
        return False

    digit = int(math.log10(num))
    rem = rem * (10 ** digit)
    num -= rem

    if num is 0:
        return True

    if num < 0:
        return False

    if int(math.log10(num)) >= digit:
        return False

    return True


print(is_palindrome(19000001))
