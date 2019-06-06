import unittest
from leetcode.p0720.longestWordInDictionary import *


class LongestWordInDictionaryTest(unittest.TestCase):
    def test_solve_sample(self):
        s = Solution()
        words = ["w", "wo", "wor", "worl", "world"]
        expected = "world"
        self.assertEqual(expected, s.longestWord(words))

    def test_solve_sample_smallest_lexicographical(self):
        s = Solution()
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        expected = "apple"
        self.assertEqual(expected, s.longestWord(words))

    def test_solve_find_smallest_lexicographical_in_broken_prefix(self):
        s = Solution()
        words = ["w", "wor", "world", "wol", "wo"]
        expected = "wol"
        self.assertEqual(expected, s.longestWord(words))


if __name__ == '__main__':
    unittest.main()
