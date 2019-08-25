class Solution:
    def rotate(self, matrix):
        size = len(matrix) - 1
        for i in range(len(matrix) // 2):
            for j in range(i, size - i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[size - j][i]
                matrix[size - j][i] = matrix[size - i][size - j]
                matrix[size - i][size - j] = matrix[j][size - i]
                matrix[j][size - i] = tmp
