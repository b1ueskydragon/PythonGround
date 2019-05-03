import unittest
from retrospective.kmp import *


class KmpTest(unittest.TestCase):

    def test_partial_match_table(self):
        pattern = "ABABC"

        expected = [-1, 0, 0, 1, 2, 0]
        actual = partial_match_table(pattern)

        self.assertEqual(expected, actual)

    def test_partial_match_table_same_prefix_suffix(self):
        pattern = "abababcaba"

        expected = [-1, 0, 0, 1, 2, 3, 4, 0, 1, 2, 3]
        actual = partial_match_table(pattern)

        self.assertEqual(expected, actual)

    def test_kmp_search(self):
        text = "ABABABABC"
        word = "ABABC"

        expected = 4  # index of the word begins
        actual = kmp_search(text, word)

        self.assertEqual(expected, actual)

    def test_kmp_search_same_prefix_suffix(self):
        text = "ababbabcababababcabaabbb"
        word = "abababcaba"

        expected = 10
        actual = kmp_search(text, word)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
