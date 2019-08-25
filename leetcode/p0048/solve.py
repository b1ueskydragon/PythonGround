class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        edge = len(matrix) - 1
        for i in range(len(matrix) // 2):
            for j in range(i, edge - i):
                tmp1 = matrix[j][edge - i]
                tmp2 = matrix[edge - i][edge - j]
                tmp3 = matrix[edge - j][i]
                tmp4 = matrix[i][j]

                matrix[j][edge - i] = tmp4
                matrix[edge - i][edge - j] = tmp1
                matrix[edge - j][i] = tmp2
                matrix[i][j] = tmp3
