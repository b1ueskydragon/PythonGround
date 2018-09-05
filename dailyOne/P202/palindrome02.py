import math


def is_palindrome(num):
    rem = num % 10
    num //= 10

    digit = int(math.log10(num))
    rem = rem * (10 ** digit)

    num = num - rem

    return rem, num


print(is_palindrome(52325))
