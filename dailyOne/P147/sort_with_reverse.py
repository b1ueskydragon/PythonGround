def reverse(lst, i, j):
    """
    care only [i:j+1]. 他範囲は気にしない.

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


lst = [3, 1, 2, 6, 8, 7, 9]
i, j = 2, 4
print(reverse(lst, i, j))


# TODO use more space
def sort_with_reverse(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] > lst[right]:
            lst = reverse(lst, left, right)
        else:
            right -= 1

    return lst
