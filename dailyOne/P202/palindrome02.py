"""
Using subtraction should be avoided.
 - if most significant digit is 0, loss of significant digits occurs.
 - e.g) 909909
        909909 % 10 = 9
        909909 // 10 = 90990
        90990 - 90000 = (0)990
"""


def is_palindrome(num):
    digit = 1
    while (num // digit) >= 10:
        digit *= 10

    most = num // digit
    least = num % 10
    if most != least:
        return False

    return True


print(is_palindrome(909909))
