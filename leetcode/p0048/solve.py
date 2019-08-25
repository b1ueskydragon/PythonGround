class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix) - 1
        row = 0
        column = 0

        move_to = matrix[0][1]
        matrix[0][1] = matrix[0][0]
        next_move_to = matrix[1][1]
        matrix[1][1] = move_to
        matrix[0][0] = matrix[1][0]
        matrix[1][0] = next_move_to
