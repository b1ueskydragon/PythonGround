"""
Sliding Window. O(N) time.
"""


def length_of_longest_subarray(xs):
    visited = set()  # additional space
    res = 0
    i, j = 0, 0
    while j < len(xs):
        # try to move j for spread range.
        if xs[j] not in visited:
            visited.add(xs[j])
            j += 1
            res = max(res, j - i)
        else:
            visited.remove(xs[i])  # xs[j] already visited the point where xs[i] is.
            i += 1  # the new start point of the range.
    return res
