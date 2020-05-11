import unittest

from .solve import canPermutePalindrome


class CanPermutePalindromeTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(canPermutePalindrome('carrace'))
        self.assertTrue(canPermutePalindrome('aaabba'))
        self.assertTrue(canPermutePalindrome('aab'))
        self.assertTrue(canPermutePalindrome('carerac'))
        self.assertTrue(canPermutePalindrome('abcddcba'))
        self.assertTrue(canPermutePalindrome('xxxxyyz'))
        self.assertTrue(canPermutePalindrome(''))
        self.assertTrue(canPermutePalindrome('x'))

    def test_false(self):
        self.assertFalse(canPermutePalindrome('xxxxyyza'))
        self.assertFalse(canPermutePalindrome('daily'))
        self.assertFalse(canPermutePalindrome('code'))
