def factorial(n, acc=1):
    if n < 1:
        return 0
    while n:
        acc *= n
        n -= 1
    return acc


def factorial_fold(n):
    from functools import reduce
    from operator import mul

    return reduce(mul, range(1, n + 1))


def factorial_builtin(n):
    import math
    return math.factorial(n)
