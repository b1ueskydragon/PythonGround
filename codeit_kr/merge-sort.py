def merge(list1, list2):
    """
    merge binary lists.
    each lists should be sorted.

    this yields a new merged list.

    :param list1: sorted list
    :param list2: sorted list
    :return: merged list
    """
    merged = []

    while list1 and list2:
        if list1[0] <= list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))

    while list1:
        merged.append(list1.pop(0))

    while list2:
        merged.append(list2.pop(0))

    return merged


def merge_index(list1, list2):
    """
    same as `merge`
    not pop, with index traverse
    """
    merged = []
    i1, i2 = 0, 0

    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] <= list2[i2]:
            merged.append(list1[i1])
            i1 += 1
        else:
            merged.append(list2[i2])
            i2 += 1

    while i1 < len(list1):
        merged.append(list1[i1])
        i1 += 1
    while i2 < len(list2):
        merged.append(list2[i2])
        i2 += 1

    return merged


def merge_sort(my_list):
    # edge case
    if len(my_list) < 2:
        return my_list

    # Divide recursively
    pivot = len(my_list) // 2
    lows = my_list[:pivot]
    # print(lows)
    highs = my_list[pivot:]
    # print(highs)

    # Conquer recursively
    return merge(merge_sort(lows), merge_sort(highs))


# test merge
print(merge([1, 3, 4], [-5, -4, -3, -2, 2, 8]))
print(merge_index([1, 3, 4], [-5, -4, -3, -2, 2, 8]))
print(merge([2], [1]))
print(merge_index([2], [1]))

print(merge([], [-1]))
print(merge([], [-1]))

# test merge_sort
some_list = [11, 3, 6, 4, 12, 1, 2]
print(merge_sort(some_list))
