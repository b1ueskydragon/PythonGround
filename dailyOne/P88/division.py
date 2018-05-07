def division(a, b):
    """
    O(n)
    """
    n = 0
    while a >= b:
        a -= b
        n += 1
    return n


print(division(123456789, 3))
