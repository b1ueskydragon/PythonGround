class Solution:
    def flipAndInvertImage(self, A):
        """
        1 - n == 1 ^ n
        """
        return [[(1 ^ n) for n in reversed(row)] for row in A]

    def flipAndInvertImage_inplace(self, A):
        """
        len(row) + 1

        since odd, center element in row need to be flip itself
        if even, + 1 make not sense in floor division
        """
        for row in A:
            for i in range((len(row) + 1) // 2):
                row[i], row[-1 - i] = 1 ^ row[-1 - i], 1 ^ row[i]
        return A
