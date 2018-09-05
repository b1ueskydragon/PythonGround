def is_palindrome(num):
    digit = 1
    while num > 10:
        digit *= 10
        num //= 10

    return num, digit


print(is_palindrome(9010550109))
