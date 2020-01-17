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
            prev = strobogrammatic_numbers(n - 2)
            # seeds
            a = 10 ** (n - 1) + 1
            b = 6 * 10 ** (n - 1) + 9
            c = 8 * 10 ** (n - 1) + 8
            d = 9 * 10 ** (n - 1) + 6
            for s in [a, b, c, d]:
                res.append(s)
                res.append(s + 10 ** (n // 2))
                res.append(s + 8 * 10 ** (n // 2))
                if n == 3:
                    continue  # skip a duplicate
                for x in prev:
                    res.append(s + x * 10)
    else:
        if n == 2:
            return [11, 69, 88, 96]
        else:
            # n = 4
            prev = strobogrammatic_numbers(n - 2)
            res.append(1001)  # 100001
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
