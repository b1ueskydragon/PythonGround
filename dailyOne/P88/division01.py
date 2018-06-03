def division_binary_shift(a, b):
    """
    do `division`
    without making q a string.

    :param a: dividend
    :param b: divisor
    :return: quotient
    """
    q = 0
    tmp_q = 1
    tmp_b = b
    while True:
        while a >= b:
            b <<= 1
            if a >= b:
                tmp_q <<= 1
            else:
                b >>= 1
                break
        a -= b
        q += tmp_q
        tmp_q = 1
        b = tmp_b

        if a < b:
            break

    return q


a, b = 10, 3
print(division_binary_shift(a, b))
print(a // b)
