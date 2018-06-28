# import memory_profiler
# python -m memory_profiler xxx.py

# @profile
def division_binary_shift(a, b):
    """
    a // b

    [note]
    q += sq
     since sq only could be 2^n  (n impls digit of quotient of each step),
     using OR `|` is OK. e.g 11 + 1000 = 1011

    :param a: dividend
    :param b: divisor
    :return: quotient
    """
    if a < b:
        return 0
    if b == 0:
        raise ZeroDivisionError

    q = 0
    sq = 1
    ori_b = b
    while a >= b:
        b <<= 1
        if a >= b:
            sq <<= 1
        else:
            b >>= 1
            a -= b
            q += sq
            sq = 1
            b = ori_b

    return q


a, b = 121111323, 232322
print(division_binary_shift(a, b))
print(a // b)
