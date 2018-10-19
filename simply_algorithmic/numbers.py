"""
Convert base10 to base2
"""


def convert2(num):
    """
    :param num: dividend
    :return: base2 converted
    """

    cache = []
    msb = 1  # digit

    while num > 0:
        cache.append(num % 2)
        num //= 2
        # msb *= 10

    return cache  # TODO reverse


num = 9215
print(convert2(num))  # 10001111111111
