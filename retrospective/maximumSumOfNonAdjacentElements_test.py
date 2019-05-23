import unittest
from retrospective.maximumSumOfNonAdjacentElements import *


class MaximumSumOfNonAdjacentElementsTest(unittest.TestCase):
    def test_maximum_sum_of_non_adjacent_elements_has_same_num(self):
        nums = [5, 5, 10, 100, 10, 5]
        expected = 110
        actual = maximum_sum_of_non_adjacent_elements(nums)

        self.assertEqual(expected, actual)

    def test_maximum_sum_of_non_adjacent_elements_sorted_asc(self):
        nums = [1, 2, 3]
        expected = 4
        actual = maximum_sum_of_non_adjacent_elements(nums)

        self.assertEqual(expected, actual)

    def test_maximum_sum_of_non_adjacent_pick_a_great_one(self):
        nums = [1, 99, 3]
        expected = 99
        actual = maximum_sum_of_non_adjacent_elements(nums)

        self.assertEqual(expected, actual)

    def test_maximum_sum_of_non_adjacent_elements(self):
        nums = [8, 2, 4, 1, 3, 9]
        expected = 21  # 8 + 4 + 9
        actual = maximum_sum_of_non_adjacent_elements_r(nums)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
