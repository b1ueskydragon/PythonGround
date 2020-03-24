class Solution:
    """
    Divide and conquer

    O(S) Time,
    S := the number of all characters in the array.

    O(m * log n) Space,
    (m, n) := there are n equal strings with length m in the worst case. (S := m * n).
    Since the recursion, there is a memory overhead. Recursive calls are stored in the execution stack.
    """

    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""

        def prefix(w1, w2, p=""):
            m = min(len(w1), len(w2))
            for i in range(m):  # O(m)
                if w1[i] != w2[i]:
                    break
                p += w1[i]
            return p

        def loop(xs, l, r):  # O(log n)
            if l == r:  # single range
                return xs[l]
            k = (l + r) // 2
            return prefix(loop(xs, l, k), loop(xs, k + 1, r))  # left prefix vs right prefix

        return loop(strs, 0, len(strs) - 1)
