import unittest

from leetcode.p1078.solve import *


class FindOcurrencesTest(unittest.TestCase):

    def test_sample(self):
        s = Solution()
        text = "alice is a good girl she is a good student"
        first = "a"
        second = "good"
        expected = ["girl", "student"]

        actual = s.findOcurrences(text, first, second)
        actual_ = s.findOcurrences_(text, first, second)
        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual_)

    def test_sample_double(self):
        s = Solution()
        text = "we will we will rock you"
        first = "we"
        second = "will"
        expected = ["we", "rock"]

        actual = s.findOcurrences(text, first, second)
        actual_ = s.findOcurrences_(text, first, second)
        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual_)

    def test_sample_repeat(self):
        s = Solution()
        text = "we will we will we will"
        first = "we"
        second = "will"
        expected = ["we", "we"]

        actual = s.findOcurrences(text, first, second)
        actual_ = s.findOcurrences_(text, first, second)
        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual_)


if __name__ == '__main__':
    unittest.main()
