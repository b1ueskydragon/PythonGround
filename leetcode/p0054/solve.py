"""
Print a given matrix in spiral form
"""


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        s = 0
        size = n * m
        length = 0
        while n > 0 and m > 0:
            for i in range(s, n):  # right
                if length == size: break
                res.append(matrix[s][i])
                length += 1

            n -= 1
            for i in range(s + 1, m):  # down
                if length == size: break
                res.append(matrix[i][n])
                length += 1

            m -= 1
            for i in reversed(range(s, n)):  # left
                if length == size: break
                res.append(matrix[m][i])
                length += 1

            for i in reversed(range(s + 1, m)):  # up
                if length == size: break
                res.append(matrix[i][s])
                length += 1

            s += 1
        return res
