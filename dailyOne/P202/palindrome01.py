def is_palindrome(num):
    """
    Run O(N)
    Space O(N) ?
    """
    curr = num  # tmp
    stack = 0  # reversed

    while curr:
        stack = stack * 10 + curr % 10
        curr //= 10

    return num == stack


print(is_palindrome(int(input())))
