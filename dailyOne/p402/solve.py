def strobogrammatic_numbers(n):
    """
    DP solution

    :param n: digits
    :return: strobogrammatic numbers with N digits
    """

    def _rec(_n, curr):
        res = []
        if _n == 0:  # base case even
            return ['']
        if _n == 1:  # base case odd
            return [0, 1, 8]
        else:
            prev = _rec(_n - 2, curr)
            for middle in prev:
                if _n < curr:
                    res.append(f'0{middle}0')  # zero-fill to [0, 1, 8] or ['']
                res.append(int(f'1{middle}1'))
                res.append(int(f'6{middle}9'))
                res.append(int(f'8{middle}8'))
                res.append(int(f'9{middle}6'))
        return res

    return _rec(n, n)
