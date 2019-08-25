class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix) - 1
        for i in range(len(matrix) // 2):
            for j in range(i, size - i):
                tmp1 = matrix[j][size - i]
                tmp2 = matrix[size - i][size - j]
                tmp3 = matrix[size - j][i]
                tmp4 = matrix[i][j]

                matrix[j][size - i] = tmp4
                matrix[size - i][size - j] = tmp1
                matrix[size - j][i] = tmp2
                matrix[i][j] = tmp3
