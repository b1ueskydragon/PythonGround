"""
create all possible strings by using 'a', 'e', 'i', 'o', 'u'.
Use the characters exactly once
"""


def permutation_builtin(xs):
    import itertools
    return list(map(list, itertools.permutations(xs)))


def permutation(xs):
    if not xs:
        return [[]]
    res = []
    for i, h in enumerate(xs):
        rems = xs[:i] + xs[i + 1:]
        for tail in permutation(rems):  # reuse previous result
            res.append([h] + tail)
    return res
