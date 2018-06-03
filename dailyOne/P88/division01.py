def division_binary_shift(a, b):
    """
    do `division`
    without making q a string.

    :param a: dividend
    :param b: divisor
    :return: quotient
    """

    d = 5  # digit capacity max
    q = 1
    tmp = q
    # r = a  # remainder (init: まだ何も割ってない状態)
    while a >= b:
        pre_a = a
        a -= (b << d)
        if a > 0:
            q <<= 1
        else:
            a = pre_a

        d -= 1

    return q


a, b = 100, 3
print(division_binary_shift(a, b))
print(a // b)
