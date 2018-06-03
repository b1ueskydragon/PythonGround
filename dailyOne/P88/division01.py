def division_binary_shift(a, b):
    """
    do `division`
    without making q a string.

    :param a: dividend
    :param b: divisor
    :return:
    """
    # d = 5  # digit capacity max
    # r = a  # remainder (init: まだ何も割ってない状態)
    # b = b << d
    tmp = b
    q = 0
    while a > b:
        b = b << 1
        while b < a:
            b = b << 1
            q += 1
        else:
            b = b >> 1

        a = a - b
        b = tmp

    return q, b << q


a, b = 100, 3
print(division_binary_shift(a, b))
print(a // b)
