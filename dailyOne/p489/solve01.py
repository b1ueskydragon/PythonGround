"""
Sliding Window's worst was O(2N), strictly. Improve to O(N), strictly.

Remind, xs[i] pass the element that xs[j] already passed.
"""


def length_of_longest_subarray(xs):
    visited = {}  # key is x, {x: x ∈ xs}. cache the most recently position where x was.
    res = 0
    i = 0
    for j, x in enumerate(xs):
        if x in visited:
            i = max(i, visited[x] + 1)
        visited[x] = j  # we can move j (and cache the element) every time.
        res = max(res, j - i + 1)
    return res
