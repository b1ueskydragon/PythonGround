class Solution:
    def flipAndInvertImage(self, A):
        """
        1 - n == 1 ^ n
        """
        return [[(1 ^ n) for n in reversed(lst)] for lst in A]
