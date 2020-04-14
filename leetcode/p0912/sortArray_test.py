import unittest
from leetcode.p0912.merge_sort import Solution as MgA
from leetcode.p0912.merge_sort01 import Solution as MgB
from leetcode.p0912.quick_sort import Solution as Qs


class SortArrayTest(unittest.TestCase):
    def test_has_duplication_and_also_negative_number(self):
        mgA = MgA()
        mgB = MgB()
        qs = Qs()
        nums = [50000, 0, -50000, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]
        expected = list(sorted(nums))
        self.assertEqual(expected, mgA.sortArray(nums.copy()))
        self.assertEqual(expected, mgB.sortArray(nums.copy()))
        self.assertEqual(expected, qs.sortArray(nums.copy()))
        self.assertNotEqual(expected, nums)

    def test_two_elements(self):
        mgA = MgA()
        mgB = MgB()
        qs = Qs()
        nums = [1, -1]
        expected = list(sorted(nums))
        self.assertEqual(expected, mgA.sortArray(nums.copy()))
        self.assertEqual(expected, mgB.sortArray(nums.copy()))
        self.assertEqual(expected, qs.sortArray(nums.copy()))
        self.assertNotEqual(expected, nums)

    def test_single_element(self):
        mgA = MgA()
        mgB = MgB()
        qs = Qs()
        nums = [0]
        expected = list(sorted(nums))
        self.assertEqual(expected, mgA.sortArray(nums.copy()))
        self.assertEqual(expected, mgB.sortArray(nums.copy()))
        self.assertEqual(expected, qs.sortArray(nums.copy()))

    def test_empty(self):
        mgA = MgA()
        mgB = MgB()
        qs = Qs()
        nums = []
        expected = list(sorted(nums))
        self.assertEqual(expected, mgA.sortArray(nums.copy()))
        self.assertEqual(expected, mgB.sortArray(nums.copy()))
        self.assertEqual(expected, qs.sortArray(nums.copy()))
