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


def has_fixed_point(ary):
    """
    O(logN)
    binary search - use `sorted` array (Narrowing down)
                  - pointer left to center, right to center
    """
    low, high = 0, len(ary)  # index

    while low <= high:
        # dynamic pivot - odd or even does not matter.
        pivot = (low + high) // 2
        if ary[pivot] == pivot:
            return pivot
        elif ary[pivot] < pivot:
            low += 1
        else:
            high -= 1
    return False


target = [-3, -2, -1, 0, 1, 2, 3, 5, 6, 7, 10, 37, 38, 40, 41, 43,
          50, 56, 60, 61, 62, 68, 80, 83, 84, 85, 87, 92, 96, 99]

print(linear_search(target))
print(has_fixed_point(target))
