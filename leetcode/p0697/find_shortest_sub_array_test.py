from unittest import TestCase

from .solve import Solution as A
from .solve01 import Solution as B


# nums.length will be between 1 and 50,000.
class FindShortestSubArrayTest(TestCase):
    def test_big_array(self):
        a, b = A(), B()
        nums = [27745, 27518, 4612, 99, 29175, 5310, 38265, 99, 99, 23079, 42208, 37513, 18112, 23627, 99, 41755, 99,
                99, 10797, 28407, 29146, 11707, 99, 99, 42650, 12111, 99, 36290, 32890, 10637, 1963, 99, 99, 99, 99,
                33323, 99, 28120, 99, 11634, 12828, 36784, 3898, 94, 33697, 99, 39871, 28950, 99, 99, 99, 99, 99, 99,
                99, 99, 19294, 19762, 15189, 33559, 18085, 41715, 99, 99, 99, 99, 99, 38143, 27856, 99, 9949, 99, 99,
                2575, 99, 99, 99, 99, 99, 99, 99, 99, 6319, 28964, 99, 43587, 14981, 99, 99, 34885, 34898, 99, 99, 2467,
                45751]
        self.assertEqual(90, b.findShortestSubArray(nums.copy()))
        self.assertEqual(90, a.findShortestSubArray(nums.copy()))

    def test_complex_duplicated(self):
        a, b = A(), B()
        nums = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2,
                2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3]
        self.assertEqual(32, b.findShortestSubArray(nums.copy()))
        self.assertEqual(32, a.findShortestSubArray(nums.copy()))

    def test_single_element(self):
        a, b = A(), B()
        nums = [44]
        self.assertEqual(1, b.findShortestSubArray(nums.copy()))
        self.assertEqual(1, a.findShortestSubArray(nums.copy()))
