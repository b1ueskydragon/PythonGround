import unittest

from leetcode.p1078.solve import *


class FindOcurrencesTest(unittest.TestCase):

    def test_sample(self):
        s = Solution()
        text = "alice is a good girl she is a good student"
        first = "a"
        second = "good"
        expected = ["girl", "student"]

        self.assertEqual(expected, s.findOcurrences(text, first, second))

    def test_sample_repeat(self):
        s = Solution()
        text = "we will we will rock you"
        first = "we"
        second = "will"
        expected = ["we", "rock"]

        self.assertEqual(expected, s.findOcurrences(text, first, second))


if __name__ == '__main__':
    unittest.main()
