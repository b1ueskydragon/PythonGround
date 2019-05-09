import unittest
from retrospective.minAddToMakeValid import *


class MinAddToMakeValidTest(unittest.TestCase):
    _VALID = 0

    def test_min_add_to_make_valid_empty(self):
        pattern = ""

        expected = self._VALID
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_balanced_closed(self):
        pattern = "{}{}"

        expected = self._VALID
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_not_balanced_separated(self):
        pattern = "{}{{{}}}"

        expected = self._VALID
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_not_balanced_included(self):
        pattern = "{{{{}}"

        expected = 2
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_not_balanced_start_open(self):
        pattern = "}}{{{{"

        expected = 6
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_not_balanced_only_open(self):
        pattern = "{{{{"

        expected = 4
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)

    def test_min_add_to_make_valid_not_balanced_only_close(self):
        pattern = "}}}"

        expected = 3
        actual = min_add_to_make_valid(pattern)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
