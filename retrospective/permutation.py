def permutation(xs, k):
    if k == 0:
        return [[]]
    res = []
    for i, x in enumerate(xs):
        _xs = permutation(xs[:i] + xs[i + 1:], k - 1)
        for _x in _xs:
            res.append([x] + _x)

    return res


def factorial(n, acc=1):
    if n < 1:
        return 0
    while n:
        acc *= n
        n -= 1
    return acc


xs = ['a', 'b', 'c', 'd']
res_k2 = list(map(''.join, permutation(xs, k=2)))
res_k3 = list(map(''.join, permutation(xs, k=3)))
# TODO test code
print(factorial(len(xs)) // factorial(len(xs) - 2), len(res_k2), res_k2)
print(factorial(len(xs)) // factorial(len(xs) - 3), len(res_k3), res_k3)
