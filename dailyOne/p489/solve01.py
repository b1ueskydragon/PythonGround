"""
Sliding Window's worst was O(2N), strictly. Improve to O(N), strictly.

Remind, xs[i] pass the element that xs[j] already passed.
"""


def length_of_longest_subarray(xs):
    start_index = {}  # x -> NEXT i
    res = 0
    i = 0
    for j, x in enumerate(xs):  # j is faster than i
        # jump i to j or not, if xs[j] in the hash map
        if x in start_index:
            i = max(i, start_index[x])
        start_index[x] = j + 1  # +1 to handle all unique case. j starts from 0 even it is faster than i.
        res = max(res, j - i + 1)
    return res
