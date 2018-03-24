import math


def first_n_step(a=int(input()), b=int(input())):
    """
    Positive integer, 1≤a,b≤10^9

    :param a: walk `a`cm per 1 second.
    :param b: `b`cm section.
    :return: minimal steps.
    """
    return math.ceil(b / a)


print(first_n_step())
