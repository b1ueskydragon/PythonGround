def three_partition(x, lst):
    """
    O(n) time and O(1) space
    :param x: pivot
    :param lst: list
    :return:
    """
    left, right = 0, 0
    last = len(lst) - 1

    while right < last:
        if lst[right] == x:
            right += 1
        elif lst[right] < x:
            swap_value(lst, left, right)
            left += 1
            right += 1
        else:
            swap_value(lst, last, right)
            last -= 1

    return lst


def swap_value(lst, i1, i2):
    lst[i1], lst[i2] = lst[i2], lst[i1]


# x, lst = 10, [9, 12, 3, 5, 14, 10, 10]
x, lst = 2, [4, 1, 1, 2, 1, 1, 3]  # TODO Bug found
print(three_partition(x, lst))
