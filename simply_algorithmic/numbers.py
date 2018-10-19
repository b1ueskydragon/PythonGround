"""
Convert base10 to base2
"""


def convert2(k):
    """
    :param k: dividend
    :return: base2 converted
    """
    msb = 1 if k else 0  # digit

    cache = 0  # output

    while k > 0:
        cache += msb * (k % 2)
        k //= 2
        msb *= 10

    return cache


num = 9215
print(convert2(num))  # 10001111111111
