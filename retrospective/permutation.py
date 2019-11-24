def permutation(xs, k):
    if k == 0:
        return [[]]
    res = []
    for i, x in enumerate(xs):
        _xs = permutation(xs[:i] + xs[i + 1:], k - 1)
        for _x in _xs:
            res.append([x] + _x)

    return res


xs = ['a', 'b', 'c', 'd']
k = 2
print(permutation(xs, 2))
