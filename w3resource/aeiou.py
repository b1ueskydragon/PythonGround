"""
create all possible strings by using 'a', 'e', 'i', 'o', 'u'.
Use the characters exactly once (permutation)
"""


def permutation_builtin(xs):
    import itertools
    return list(map(list, itertools.permutations(xs)))


def combination_builtin(xs, k):
    import itertools
    return list(map(list, itertools.combinations(xs, k)))


def permutation(xs):
    if not xs:
        return [[]]
    res = []
    for i, h in enumerate(xs):
        rems = xs[:i] + xs[i + 1:]
        for tail in permutation(rems):  # reuse previous result
            res.append([h] + tail)
    return res


def combination(xs, k):
    res = []

    def _dfs(node, i, leaf):
        if len(leaf) == k:
            res.append(leaf)
            return

        if len(node) - i + len(leaf) >= k:
            _dfs(node, i + 1, leaf + [node[i]])
            _dfs(node, i + 1, leaf)

    _dfs(xs, 0, [])
    return res
