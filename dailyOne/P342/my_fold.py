"""
O(N * f)

N is length of a list,
f is cost of call function.
"""


def foldl(xs, f, acc):
    """
    fold left
    xs is immutable, acc is mutable.

    :param xs: a list to fold
    :param f:  a binary function
    :param acc: init value of an accumulator (starting value)
    :return: folded result
    """
    for x in xs:
        acc = f(acc, x)

    return acc


def foldr(xs, f, acc):
    """
    fold right.
    xs is immutable, acc is mutable.

    :param xs: a list to fold
    :param f:  a binary function
    :param acc: init value of an accumulator (starting value)
    :return: folded result
    """

    i = len(xs) - 1
    while i >= 0:
        acc = f(xs[i], acc)
        i -= 1

    return acc


def add(a, b):
    """ Example of some `f` """
    return a + b


# test
l = [2, 5, 3, 1, 4]

print(foldl(l, add, 0))
print(foldl(l, min, l[0]))

print(foldr(l, add, 0))
print(foldr(l, min, l[0]))
