def strobogrammatic_numbers(n):
    """
    DP solution

    :param n: digits
    :return: strobogrammatic numbers with N digits
    """

    def rec(k, curr):
        res = []
        if k == 0:  # base case even
            return ['']
        if k == 1:  # base case odd
            return [0, 1, 8]
        else:
            prev = rec(k - 2, curr)
            for middle in prev:
                if k < curr:
                    res.append(f'0{middle}0')  # zero-fill to [0, 1, 8] or ['']
                res.append(int(f'1{middle}1'))
                res.append(int(f'6{middle}9'))
                res.append(int(f'8{middle}8'))
                res.append(int(f'9{middle}6'))
        return res

    result = rec(n, n)
    result.sort()  # for test
    return result
