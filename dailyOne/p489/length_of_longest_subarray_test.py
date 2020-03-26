from unittest import TestCase

from dailyOne.p489.solve import length_of_longest_subarray


class LengthOfLongestSubArrayTest(TestCase):
    def test_numbers(self):
        xs = [5, 1, 3, 5, 2, 3, 4, 1]
        self.assertEqual(5, length_of_longest_subarray(xs))  # "[5, 2, 3, 4, 1]"

    def test_substring(self):
        xs = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'b']
        self.assertEqual(3, length_of_longest_subarray(xs))  # "abc"

    def test_substring_single_element(self):
        xs = ['b'] * 5
        self.assertEqual(1, length_of_longest_subarray(xs))  # "b"

    def test_substring_not_a_subsequence(self):
        xs = ['p', 'w', 'w', 'k', 'e', 'w']
        self.assertEqual(3, length_of_longest_subarray(xs))  # "wke"

    def test_should_not_skip_too_much(self):
        xs = ['p', 'w', 'w', 'k', 'e', 'w', 'p']
        self.assertEqual(4, length_of_longest_subarray(xs))  # "kewp"
