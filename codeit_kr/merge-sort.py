def merge(list1, list2, merged=[]):
    """
    merge binary lists.
    each lists should be sorted.

    :param list1: sorted list
    :param list2: sorted list
    :param merged: result
    :return: merged list
    """
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))

    while list1:
        merged.append(list1.pop(0))

    while list2:
        merged.append(list2.pop(0))

    return merged


def merge_sort(my_list):
    pivot = len(my_list) // 2
    

# print(merge([1, 3, 4], [-5, -4, -3, -2, 2, 8]))
some_list = [11, 3, 6, 4, 12, 1, 2]
print(merge_sort(some_list))
