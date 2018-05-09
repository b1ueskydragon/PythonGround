def division_brute_force(a, b):
    """
    initial approach

    :param a: dividend
    :param b: divisor
    :return: quotient
    """
    n = 0
    while a >= b:
        a -= b
        n += 1
    return n


def division_binary_shift(a, b):
    """
    e.g.:
    28 / 5 = 11100 / 101
           = 101 x 1 x 2^2 ( a = 11100 - 10100 = 1000 )
           + 101 x 0 x 2^1 ( a =  1000 - 1010 )
           + 101 x 1 x 2^0 ( a =  1000 - 101 = 11 )

           => q = 101, r = 11

    101 << 2 + 101 << 1  = 11110 > 11100 (=> 101 << 1 should be dropped)
    101 << 2 + 101 << 0  = 11001 < 11100

    hint:
    b  x _ x 2^n  ( _ is 1 or 0 )

    101 x 2 ^ 2 x 1 = 101 << 2 x 1

    11 < 101, r < b (=> end)

    :param a: dividend
    :param b: divisor
    :return: quotient
    """

    a = a - (b << 2)
    a = a - (b << 0)

    return a


print(division_binary_shift(28, 5))
