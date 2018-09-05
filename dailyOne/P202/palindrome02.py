def is_palindrome(num):
    origin = num
    stack = 0

    while num:
        stack = num % 10 + stack * 10
        num //= 10

    return stack == origin


print(is_palindrome(int(input())))
