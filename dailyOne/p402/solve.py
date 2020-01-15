def strobogrammatic_numbers(n):
    """
    :param n: digits
    :return: strobogrammatic numbers with N digits
    """
    res = []
    if n % 2 != 0:
        if n == 1:
            return [0, 1, 8]  # 6 and 9 is excluded. yep.
        else:
            # n = 3
            prev = strobogrammatic_numbers(n - 2)
            for x in prev:
                res.append(101 + x * (10 ** (n - 2)))
            for x in prev:
                res.append(609 + x * (10 ** (n - 2)))
            for x in prev:
                res.append(808 + x * (10 ** (n - 2)))
            for x in prev:
                res.append(906 + x * (10 ** (n - 2)))
    else:
        return [11, 69, 88, 96]
    return res
