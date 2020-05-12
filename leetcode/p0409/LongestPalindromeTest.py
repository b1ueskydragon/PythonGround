import unittest

from .solve import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = Solution()
        self.assertEqual(11, a.longestPalindrome('dailycodedaily'))  # 3`d`s.
