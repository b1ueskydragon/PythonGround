class Solution:
    def flipAndInvertImage(self, A):
        """
        1 - n == 1 ^ n
        """
        res = []
        for lst in A:
            cache = []
            for n in reversed(lst):
                cache.append(1 ^ n)
            res.append(cache)

        return res
