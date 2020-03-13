import unittest

from leetcode.p0152.solve import Solution as A


class MaxProductTest(unittest.TestCase):
    def test_sample1(self):
        a = A()
        nums = [2, 3, -2, 4]
        self.assertEqual(6, a.maxProduct(nums))

    def test_sample2(self):
        a = A()
        nums = [-2, 0, -1]
        self.assertEqual(0, a.maxProduct(nums))

    def test_has_contiguous_subarray_mixed_negate_sign(self):
        a = A()
        nums = [-2, 4, -2, -3, -5, 6, -7]
        self.assertEqual(5040, a.maxProduct(nums))

    def test_begin_with_zero(self):
        a = A()
        nums = [0, 2]
        self.assertEqual(2, a.maxProduct(nums))

    def test_no_contiguous_subarray(self):
        a = A()
        nums = [3, -1, 4]
        self.assertEqual(4, a.maxProduct(nums))
