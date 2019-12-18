import unittest


class InsertionSortTest(unittest.TestCase):
    def test_odd_len_nums(self):
        nums = [11, 3, 6, 4, 12, 1, 2]
        self.assertEqual(False, True)

    def test_even_len_nums(self):
        nums = [11, 3, 6, 4, 5, 12, 1, 2]
        self.assertEqual(False, True)

    def test_has_duplicated_elements(self):
        nums = [11, 3, 6, 4, 4, 12, 1, 2, 3]
        self.assertEqual(False, True)
