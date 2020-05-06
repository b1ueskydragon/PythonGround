"""
Print a given matrix in spiral form
"""


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix: return []
        M, N = len(matrix), len(matrix[0])
        # visited = [[False] * N] * M
        visited = [[False for _ in range(N)] for _ in range(M)]
        res = []
        m, n = 0, 0
        # right, down, left, up
        d_m = [0, 1, 0, -1]
        d_n = [1, 0, -1, 0]
        # direction. retrieve in d_m and d_n
        d = 0
        for _ in range(M * N):
            res.append(matrix[m][n])  # append one element in one loop.
            visited[m][n] = True
            # set the next
            maybe_m = m + d_m[d]
            maybe_n = n + d_n[d]
            # proceed in the current direction
            if 0 <= maybe_m < M and 0 <= maybe_n < N and not visited[maybe_m][maybe_n]:
                m = maybe_m
                n = maybe_n
            else:  # change the direction
                d = (d + 1) % 4
                m = m + d_m[d]
                n = n + d_n[d]

        return res
