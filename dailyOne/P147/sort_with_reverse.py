def reverse(lst, i, j):
    """
    WIP: Implement first to use result.

    :param lst: list
    :param i: idx1
    :param j: idx2
    :return: reversed list
    """
    if j < i:
        i, j = j, i

    rlst = [k for k in reversed(lst[i:j + 1])]

    if i is 0:
        return rlst + lst[j + 1:]
    elif j is len(lst) - 1:
        return lst[:i] + rlst
    else:
        return lst[:i] + rlst + lst[j + 1:]


def sort_with_reverse(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] > lst[right]:
            lst = reverse(lst, left, right)
        else:
            right -= 1

    return lst


lst = [3, 1, 2, 5, 4]
print(sort_with_reverse(lst))
