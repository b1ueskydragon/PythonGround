class Solution:
    """
    Divide and conquer
    """

    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""

        def prefix(w1, w2, p=""):
            n = min(len(w1), len(w2))
            for i in range(n):
                if w1[i] != w2[i]:
                    break
                p += w1[i]
            return p

        def loop(xs, l, r):
            if l == r:  # single range
                return xs[l]
            if r - l == 1:  # binary range
                return prefix(xs[l], xs[r])
            k = (l + r) // 2
            return prefix(loop(xs, l, k), loop(xs, k + 1, r))  # left prefix vs right prefix

        return loop(strs, 0, len(strs) - 1)
