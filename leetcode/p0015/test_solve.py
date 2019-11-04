import unittest

from leetcode.p0015.solve import Solution as A


class ThreeSumTest(unittest.TestCase):
    def test_threeSum(self):
        a = A()
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(expected, a.threeSum(nums))
        self.assertEqual(expected, a.threeSum_improve(nums))

    def test_threeSum01(self):
        a = A()
        nums = [1, -6, 4, 2, -1, 0, 2, 0, -2, 0]
        expected = [[-1, 0, 1], [-6, 2, 4], [0, 0, 0], [-2, 0, 2]]
        self.assertEqual(expected, a.threeSum(nums))
        self.assertEqual(expected, a.threeSum_improve(nums))

    def test_threeSum_less_than_3(self):
        a = A()
        nums = [-1, 1]
        expected = []
        self.assertEqual(expected, a.threeSum(nums))
        self.assertEqual(expected, a.threeSum_improve(nums))


if __name__ == '__main__':
    unittest.main()
