import math


def first_n_step(t=input()):
    """
    walk  a cm per 1 second.
    step  b cm section.
    Positive integer, 1≤a,b≤10^9

    :param t: input text
    :return: minimal steps.
    """
    a = int(t.split(' ')[0])
    b = int(t.split(' ')[1])
    return math.ceil(b / a)


print(first_n_step())
