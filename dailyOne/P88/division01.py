def division_binary_shift(a, b):
    """
    do `division`
    without making q a string.

    :param a: dividend
    :param b: divisor
    :return: quotient
    """
    if a < b:
        return 0
    if b == 0:
        raise ZeroDivisionError

    q = 0
    tmp_q = 1
    tmp_b = b
    while a >= b:
        b <<= 1
        if a >= b:
            tmp_q <<= 1
        else:
            b >>= 1
            a -= b
            q += tmp_q
            tmp_q = 1
            b = tmp_b

    return q


a, b = 10, 3
print(division_binary_shift(a, b))
print(a // b)

a, b = 121111323, 232322
print(division_binary_shift(a, b))
print(a // b)
