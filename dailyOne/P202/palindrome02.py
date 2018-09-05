import math

digit = lambda k: int(math.log10(k)) if k > 0 else 0


# TODO Do not use log10 to find digit
def is_palindrome(num):
    while num:
        if num < 0:
            return False

        rem = num % 10
        num //= 10

        if num is 0:
            return True
        if rem is 0:
            return False

        bef = digit(num)
        rem = rem * (10 ** bef)
        num -= rem
        aft = digit(num)

        if num < 0:
            return False

        if aft is bef:
            return False

    return True


print(is_palindrome(1010550101))
