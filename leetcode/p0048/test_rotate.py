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


if __name__ == '__main__':
    unittest.main()
