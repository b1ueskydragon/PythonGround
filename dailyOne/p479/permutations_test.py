import itertools
from unittest import TestCase

from dailyOne.p479.solve import permutations


class PermutationsTest(TestCase):
    def test_length_3(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(expected, permutations(nums))

    def test_empty(self):
        self.assertEqual([[]], permutations([]))

    def test_single_element(self):
        self.assertEqual([[1]], permutations([1]))

    def test_length_2(self):
        nums = [1, 2]
        self.assertEqual([[1, 2], [2, 1]], permutations(nums))

    def test_length_7(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        expected = list(map(list, itertools.permutations(nums)))
        self.assertEqual(expected, permutations(nums))
