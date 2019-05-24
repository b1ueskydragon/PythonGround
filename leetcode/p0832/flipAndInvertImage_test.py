import unittest
from leetcode.p0832.solve import *


class FlipAndInvertImage(unittest.TestCase):
    s = Solution()

    def test_flipAndInvertImage_R3(self):
        matrix = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        actual = self.s.flipAndInvertImage(matrix)

        self.assertEqual(expected, actual)

    def test_flipAndInvertImage_R4(self):
        matrix = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        expected = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        actual = self.s.flipAndInvertImage(matrix)

        self.assertEqual(expected, actual)

    def test_flipAndInvertImage_zero(self):
        matrix = [[]]
        expected = [[]]
        actual = self.s.flipAndInvertImage(matrix)

        self.assertEqual(expected, actual)

    def test_flipAndInvertImage_inplace_R3(self):
        matrix = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
        expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        actual = self.s.flipAndInvertImage_inplace(matrix)

        self.assertEqual(expected, actual)

    def test_flipAndInvertImage_inplace_R4(self):
        matrix = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        expected = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        actual = self.s.flipAndInvertImage_inplace(matrix)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
