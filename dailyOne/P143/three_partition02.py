def three_partition(x, lst):
    """
    O(n) time and O(1) space
    :param x: pivot
    :param lst: list
    :return:
    """
    left, right = 0, 0
    center = len(lst) - 1

    while left < right:
        if lst[right] == x:
            pass
        elif lst[right] < x:
            pass
        else:
            pass

    return lst
