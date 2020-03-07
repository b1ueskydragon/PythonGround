import unittest

from dailyOne.p470.solve import theNearestLargeNumber


class TheNearestLargeNumberTest(unittest.TestCase):
    def test_at_the_beginning(self):
        nums = [4, 1, 3, 5, 6]
        i = 0
        self.assertEqual(3, theNearestLargeNumber(nums, i))

    def test_return_any_one_of_them(self):
        nums = [4, 1, 3, 5, 6]
        i = 1
        self.assertEqual(0, theNearestLargeNumber(nums, i))  # or 2

    def test_i_is_in_middle(self):
        nums = [4, 1, 3, 5, 6]
        i = 2
        self.assertEqual(3, theNearestLargeNumber(nums, i))

    def test_adjacent_one(self):
        nums = [4, 1, 3, 5, 6]
        i = 3
        self.assertEqual(4, theNearestLargeNumber(nums, i))

    def test_there_is_not_any_large_num(self):
        nums = [4, 1, 3, 5, 6]
        i = 4
        self.assertIsNone(theNearestLargeNumber(nums, i))

    def test_sample(self):
        nums = [4, 5, 1]
        i = 0
        self.assertEqual(1, theNearestLargeNumber(nums, i))
