def reverse(lst, i, j):
    """reverse section in-place"""
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


def max_idx(lst):
    """current index of max value"""
    return lst.index(max(lst))


def sort(lst):
    """sort using `reverse` in-place"""
    # TODO
    return lst


lst = [9, 8, 1, 2, 8, 7, 4, 5, 8, 6, 1, 2]
print(len(lst))
print(max_idx(lst))
print(sort(lst))
