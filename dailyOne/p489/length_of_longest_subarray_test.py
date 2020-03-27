from unittest import TestCase

from dailyOne.p489.solve import length_of_longest_subarray as a


class LengthOfLongestSubArrayTest(TestCase):
    def test_numbers(self):
        xs = [5, 1, 3, 5, 2, 3, 4, 1]  # [5, 2, 3, 4, 1]
        self.assertEqual(5, a(xs))

    def test_substring(self):
        xs = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b']  # "abc"
        self.assertEqual(3, a(xs))

    def test_substring_single_element(self):
        xs = ['b'] * 5  # "b"
        self.assertEqual(1, a(xs))

    def test_substring_not_a_subsequence(self):
        xs = ['p', 'w', 'w', 'k', 'e', 'w']  # "wke"
        self.assertEqual(3, a(xs))

    def test_should_not_skip_too_much(self):
        xs = ['p', 'w', 'w', 'k', 'e', 'w', 'p']  # "kewp"
        self.assertEqual(4, a(xs))
