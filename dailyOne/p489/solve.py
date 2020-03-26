"""
Given an array of elements, return the length of the longest subarray where all its elements are distinct.
For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""


def length_of_longest_subarray(xs):
    if not xs:
        return 0

    def is_all_unique(i, j, ary):
        a = ary[i:j + 1]  # additional space
        return len(a) == len(set(a))

    prev, curr = 1, 1
    l, r = 0, 1  # r is faster
    while r < len(xs):
        if is_all_unique(l, r, xs):
            curr = r - l + 1
        else:
            prev = max(curr, prev)
            curr = 1
            l += 1
        r += 1
    return max(curr, prev)
