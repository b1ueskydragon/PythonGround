import unittest
from leetcode.p0912.merge_sort import Solution as Mg
from leetcode.p0912.quick_sort import Solution as Qs


class SortArrayTest(unittest.TestCase):
    def test_has_duplication_and_also_negative_number(self):
        mg = Mg()
        qs = Qs()
        nums = [50000, 0, -50000, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.assertEqual(list(sorted(nums)), mg.sortArray(nums))
        self.assertEqual(list(sorted(nums)), qs.sortArray(nums))

    def test_two_elements(self):
        mg = Mg()
        qs = Qs()
        nums = [1, -1]
        self.assertEqual(list(sorted(nums)), mg.sortArray(nums))
        self.assertEqual(list(sorted(nums)), qs.sortArray(nums))

    def test_single_element(self):
        mg = Mg()
        qs = Qs()
        nums = [0]
        self.assertEqual(list(sorted(nums)), mg.sortArray(nums))
        self.assertEqual(list(sorted(nums)), qs.sortArray(nums))

    def test_empty(self):
        mg = Mg()
        qs = Qs()
        nums = []
        self.assertEqual(list(sorted(nums)), mg.sortArray(nums))
        self.assertEqual(list(sorted(nums)), qs.sortArray(nums))
