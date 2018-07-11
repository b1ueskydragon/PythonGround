def reverse(lst, i, j):
    """
    focus on only [i:j+1]
    do not focus the others.

    :param lst: list
    :param i: idx1
    :param j: idx2
    :return: reversed list
    """
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


def sort(lst, last):
    """
    ある程度`正しい`場所を事前に決めて行う.

    :param lst:
    :return:
    """
    if not last:  # exit case (last is 0)
        return lst

    left, right = 0, last
    while left < right:
        if lst[left] > lst[right]:
            lst = reverse(lst, left, right)
        else:
            if lst[right] > lst[last]:  # keep max value on last.
                lst[right], lst[last] = lst[last], lst[right]
            right -= 1
    return sort(lst, last - 1)


# lst = [3, 1, 2, 5, 4]
# lst = [3, 1, 2, 6, 8, 5, 7]
lst = [1, 2, 3, 6, 5, 4, 1, 2, 7, 1]
print(sort(lst, len(lst) - 1))
