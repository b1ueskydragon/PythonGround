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
res_k2 = list(map(''.join, permutation(xs, k=2)))
res_k3 = list(map(''.join, permutation(xs, k=3)))
# TODO calc length  n! / (n-k)!
# TODO test code
print(len(res_k2), res_k2)
print(len(res_k3), res_k3)
