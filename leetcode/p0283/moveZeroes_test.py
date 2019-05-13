import unittest
from leetcode.p0283.solve import Solution


class MoveZerosTest(unittest.TestCase):
    def test_move_zeros(self):
        s = Solution()

        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]

        s.moveZeroes(nums)
        actual = nums

        self.assertEqual(expected, actual)

    def test_move_zeros_one_zero(self):
        s = Solution()

        nums = [1, 0, 3, 4, 5]
        expected = [1, 3, 4, 5, 0]

        s.moveZeroes(nums)
        actual = nums

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
