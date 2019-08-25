class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix) - 1
        i = 0  # row
        j = 0  # column
        tmp1 = matrix[j][size - i]  # 0, 1
        tmp2 = matrix[size - i][size - j]  # 1, 1
        tmp3 = matrix[size - j][i]  # 1,0
        tmp4 = matrix[i][j]  # 0, 0

        matrix[j][size - i] = tmp4
        matrix[size - i][size - j] = tmp1
        matrix[size - j][i] = tmp2
        matrix[i][j] = tmp3
