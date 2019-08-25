import unittest

from leetcode.p0048.solve import Solution as A


class RotateTest(unittest.TestCase):
    def test_rotate_2x2(self):
        a = A()
        matrix = [
            [1, 2],
            [4, 5]
        ]
        expected = [
            [4, 1],
            [5, 2]
        ]
        a.rotate(matrix)  # in-place
        self.assertEqual(expected, matrix)

    def test_rotate_3x3(self):
        a = A()
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        a.rotate(matrix)
        self.assertEqual(expected, matrix)

    def test_rotate_4x4(self):
        a = A()
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        expected = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        a.rotate(matrix)
        self.assertEqual(expected, matrix)


if __name__ == '__main__':
    unittest.main()
