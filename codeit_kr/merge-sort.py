def merge(list1, list2, merged=[]):
    """
    merge binary lists.
    each lists should be sorted.

    :param list1: sorted list
    :param list2: sorted list
    :param merged: result
    :return: merged list
    """
    ran = min(len(list1), len(list2))
    i1 = i2 = 0
    while i1 < ran and i2 < ran:
        if list1[i1] <= list2[i2]:
            merged.append(list1[i1])
            i1 += 1
        else:
            merged.append(list2[i2])
            i2 += 1

    while i1 < ran:
        merged.append(list1[i1])
        i1 += 1

    while i2 < ran:
        merged.append(list2[i2])
        i2 += 1

    return merged


print(merge([1, 3, 4], [2, 2, 3, 5]))


def merge_sort(my_list):
    return


some_list = [11, 3, 6, 4, 12, 1, 2]
print(merge_sort(some_list))
