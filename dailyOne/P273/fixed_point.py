"""
Condition: given a sorted array
"""


def linear_search(ary):
    """
    linear foreach.
    O(N) - n is an length of array.
    """
    for i, e in enumerate(ary):
        if i == e:
            return i
    return False


def has_fixed_point_b(ary):
    """
    O(logN)

    use `sorted` array (Pruning).
    TODO: binary search recursion (split, split ...)

    TODO: imagine differential graph

    TODO: use set edition to find missing part?
    """
    pivot = len(ary) // 2  # odd or even does not matter.
    p_val = ary[pivot]

    print(pivot, p_val)

    if p_val < pivot:
        ary = ary[:pivot]
    else:
        ary = ary[pivot:]

    linear_search(ary)

    return pivot if p_val == pivot else False


# given_t = [-6, 0, 2, 40]
# given_f = [1, 5, 7, 8]
#
# print(linear_search(given_t))
# print(linear_search(given_f))

# print(has_fixed_point_b(given_t))
# print(has_fixed_point_b(given_f))

# import random
# target = list(sorted(random.sample(range(100), 30)))

target = [-3, -2, -1, 0, 1, 2, 3, 5, 6, 7, 10, 37, 38, 40, 41, 43,
          50, 56, 60, 61, 62, 68, 80, 83, 84, 85, 87, 92, 96, 99]

print(linear_search(target))
print(has_fixed_point_b(target))  # TODO fix bug
