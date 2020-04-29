import unittest

from leetcode.p0053.solve import Solution as A


class MaxSubArrayTest(unittest.TestCase):
    """
    containing at least one number.
    """

    def test_singular(self):
        a = A()
        nums = [99]
        self.assertEqual(99, a.maxSubArray(nums))

    def test_with_negate_numbers(self):
        a = A()
        nums = [-1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1]
        self.assertEqual(2, a.maxSubArray(nums))

    def test_big_numbers(self):
        a = A()
        nums = [-27745, 27518, 54612, -2, 79175, -55310, -38265, -2, -2, 73079, -42208, 37513, 18112, -73627, -2, 91755,
                -2, -2, -60797, -78407, 29146, 11707, -2, -2, -42650, -12111, -2, -36290, 82890, 60637, 51963, 2, -2,
                -2, -2, 83323, -2, 78120, -2, -61634, -12828, 36784, 53898, -50094, -83697, -2, -89871, -28950, -2, -2,
                -2, -2, -2, -2, -2, -2, -69294, -69762, 65189, 83559, 68085, 41715, -2, -2, -2, -2, -2, -88143, -27856,
                -2, 9949, -2, -2, 2575, -2, -2, -1, -1, 2, 99, 0, -2, -6319, -78964, -2, -43587, -14981, -2, -2, 84885,
                84898, 2, -2, -2467, -95751]
        self.assertEqual(373145, a.maxSubArray(nums))


if __name__ == '__main__':
    unittest.main()
