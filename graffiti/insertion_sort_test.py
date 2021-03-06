import unittest

from graffiti.insertion_sort import insertion_sort, insertion_sort_desc


class InsertionSortTest(unittest.TestCase):
    def test_odd_len_nums(self):
        nums = [11, 3, 6, 4, 12, 1, 2]
        self.assertEqual(list(sorted(nums)), insertion_sort(nums))

    def test_even_len_nums(self):
        nums = [11, 3, 6, 4, 5, 12, 1, 2]
        self.assertEqual(list(sorted(nums)), insertion_sort(nums))

    def test_has_duplicated_elements(self):
        nums = [11, 3, 6, 4, 4, 12, 1, 2, 3]
        self.assertEqual(list(sorted(nums)), insertion_sort(nums))

    def test_empty(self):
        nums = []
        self.assertEqual(list(sorted(nums)), insertion_sort(nums))

    def test_single_element(self):
        nums = [-1]
        self.assertEqual(list(sorted(nums)), insertion_sort(nums))

    def test_insertion_sort_desc(self):
        nums = [5, 4, 1, 2, 3]
        self.assertEqual(list(sorted(nums, reverse=True)), insertion_sort_desc(nums))

    def test_has_duplicated_elements_desc(self):
        nums = [11, 3, 6, 4, 4, 12, 1, 2, 3]
        self.assertEqual(list(sorted(nums, reverse=True)), insertion_sort_desc(nums))
