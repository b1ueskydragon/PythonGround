import unittest
from retrospective.minAddToMakeValid import *


class KmpTest(unittest.TestCase):

    def test_min_add_to_make_valid_balanced(self):
        pattern = "((())"

        expected = 1
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_balanced_closed(self):
        pattern = "()()"

        expected = 0
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_not_balanced(self):
        pattern = "()((()))"

        expected = 0
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_not_balanced_open(self):
        pattern = "))(((("

        expected = 6
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)
