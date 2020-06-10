import unittest

from .largest_sum_of_non_adjacent import largest_sum_of_non_adjacent


class LargestSumOfNonAdjacent(unittest.TestCase):
    def test_pos_nums_1(self):
        self.assertEqual(13, largest_sum_of_non_adjacent([2, 4, 6, 2, 5]))

    def test_pos_nums_2(self):
        self.assertEqual(10, largest_sum_of_non_adjacent([5, 1, 1, 5]))

    def test_pos_and_neg_nums_1(self):
        self.assertEqual(6, largest_sum_of_non_adjacent([5, 1, 1, -5]))

    def test_zeros_and_pos_and_neg_nums(self):
        self.assertEqual(1, largest_sum_of_non_adjacent([0, 0, 0, -2, 0, 0, 1, 1, 0]))

    def test_negs_and_zero(self):
        self.assertEqual(0, largest_sum_of_non_adjacent([-1, -2, -3, 0, -4, -1, -4, -5]))

    def test_negs(self):
        self.assertEqual(-1, largest_sum_of_non_adjacent([-2, -3, -4, -1, -4, -5]))

    def test_all(self):
        self.assertEqual(103, largest_sum_of_non_adjacent([-1, 1, -1, 2, -2, 0, 1, -99, 99]))
