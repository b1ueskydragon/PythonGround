def pow_itr(x, n):
    """
    O(log n)

    use much less space than recursion
      - no recursing down that call stack
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x


print(pow_itr(3, 51))


def pow_tail(x, y):
    """
    tail rec style
    """
    if y == 0:
        return 1
    if y % 2 != 0:
        return x * pow_tail(x, y - 1)
    else:
        return pow_tail(x ** 2, y // 2)


print(pow_tail(3, 51))
