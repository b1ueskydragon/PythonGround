def has_fixed_point_l(ary):
    """
    linear foreach.
    O(N) - n is an length of array.
    """
    for i, e in enumerate(ary):
        if i == e:
            return i
    return False


def has_fixed_point_s(ary):
    """
    TODO:
    use Set.
    binary search (pointer left and right).

    TODO:
    use `sorted` array (Pruning).
    """
    size = len(ary)  # Make a set with max len? - not sorted one
    pivot = size // 2 if size % 2 != 0 else size // 2 - 1

    return


# given a sorted array
given_t = [-6, 0, 2, 40]
given_f = [1, 5, 7, 8]

print(has_fixed_point_l(given_t))
print(has_fixed_point_l(given_f))

print(has_fixed_point_s(given_t))
print(has_fixed_point_s(given_f))
