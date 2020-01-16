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
        if n == 2:
            return [11, 69, 88, 96]
        else:
            # n = 4
            prev = strobogrammatic_numbers(n - 2)
            res.append(1001) # 100001
            for x in prev:
                res.append(1001 + x * 10)
            res.append(6009)
            for x in prev:
                res.append(6009 + x * 10)
            res.append(8008)
            for x in prev:
                res.append(8008 + x * 10)
            res.append(9006)
            for x in prev:
                res.append(9006 + x * 10)
    return res
