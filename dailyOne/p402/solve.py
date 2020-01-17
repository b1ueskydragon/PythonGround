def strobogrammatic_numbers(n):
    """
    :param n: digits
    :return: strobogrammatic numbers with N digits
    """
    res = []
    if n % 2 != 0:
        if n == 1:
            return [0, 1, 8]  # 6 and 9 is excluded. yep.
        elif n == 3:
            return [101, 111, 181,
                    609, 619, 689,
                    808, 818, 888,
                    906, 916, 986]
        else:
            prev = strobogrammatic_numbers(n - 2)
            a = 10 ** (n - 1) + 1
            res.append(a)
            res.append(a + 10 ** (n // 2))
            res.append(a + 8 * 10 ** (n // 2))
            for x in prev:
                res.append(a + x * 10)

            b = 6 * 10 ** (n - 1) + 9
            res.append(b)
            res.append(b + 10 ** (n // 2))
            res.append(b + 8 * 10 ** (n // 2))

            for x in prev:
                res.append(b + x * 10)

            c = 8 * 10 ** (n - 1) + 8
            res.append(c)
            res.append(c + 10 ** (n // 2))
            res.append(c + 8 * 10 ** (n // 2))
            for x in prev:
                res.append(c + x * 10)

            d = 9 * 10 ** (n - 1) + 6
            res.append(d)
            res.append(d + 10 ** (n // 2))
            res.append(d + 8 * 10 ** (n // 2))
            for x in prev:
                res.append(d + x * 10)
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
