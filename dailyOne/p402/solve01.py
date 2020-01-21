def strobogrammatic_numbers(n):
    def rec(k, curr):
        res = []
        if k == 0:  # base case even
            return [0]
        if k == 1:  # base case odd
            return [0, 1, 8]
        else:
            prev = rec(k - 2, n)
            for middle in prev:
                if k < curr:
                    res.append(middle * 10)
                # seeds
                a = 10 ** (k - 1) + 1
                b = 6 * 10 ** (k - 1) + 9
                c = 8 * 10 ** (k - 1) + 8
                d = 9 * 10 ** (k - 1) + 6
                res.append(a + middle * 10)
                res.append(b + middle * 10)
                res.append(c + middle * 10)
                res.append(d + middle * 10)
        return res

    result = rec(n, n)
    result.sort()  # for test
    return result
