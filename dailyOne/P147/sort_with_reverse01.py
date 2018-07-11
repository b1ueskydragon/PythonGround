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
    """
    sort using `reverse` in-place

    Time: O(n^2)
    Space: O(1)

    探索 range を1ずつ縮めていきながら,
    もっとも大きい value を一度先頭に送り, 末尾に来させる.
    """
    for idx in reversed(range(len(lst))):
        reverse(lst, 0, max_idx(lst[:idx + 1]))
        reverse(lst, 0, idx)
    return lst


lst = [2, 5, 3, 1, 4]
print(sort(lst))
