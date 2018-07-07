"""
partition the list into three parts.
[less than, equal, larger than]
Ordering within a part can be arbitrary.
"""


def three_partition(x, lst):
    """
    Simply edition.
    O(n)

    :param x: pivot
    :param lst: list
    :return:
    """
    less, equal, large = [], [], []
    for k in lst:
        if k < x:
            less.append(k)
        elif k > x:
            large.append(k)
        else:
            equal.append(k)

    return less + equal + large


x, lst = 10, [9, 12, 3, 5, 14, 10, 10]
print(three_partition(x, lst))
