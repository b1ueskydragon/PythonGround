import unittest

from leetcode.p0020.solve import Solution
from leetcode.p0020.solve01 import Solution as Solution01


class IsValidTest(unittest.TestCase):
    def test_empty(self):
        s = Solution()
        s01 = Solution01()

        brackets = ""
        self.assertEqual(True, s.isValid(brackets))
        self.assertEqual(True, s01.isValid(brackets))

    def test_case01(self):
        s = Solution()
        s01 = Solution01()

        brackets = "()"
        self.assertEqual(True, s.isValid(brackets))
        self.assertEqual(True, s01.isValid(brackets))

    def test_case02(self):
        s = Solution()
        s01 = Solution01()

        brackets = "()[]{}"
        self.assertEqual(True, s.isValid(brackets))
        self.assertEqual(True, s01.isValid(brackets))

    def test_case03(self):
        s = Solution()
        s01 = Solution01()

        brackets = "(]"
        self.assertEqual(False, s.isValid(brackets))
        self.assertEqual(False, s01.isValid(brackets))

    def test_case04(self):
        s = Solution()
        s01 = Solution01()

        brackets = "([)]"
        self.assertEqual(False, s.isValid(brackets))
        self.assertEqual(False, s01.isValid(brackets))

    def test_case05(self):
        s = Solution()
        s01 = Solution01()

        brackets = "{[]}"
        self.assertEqual(True, s.isValid(brackets))
        self.assertEqual(True, s01.isValid(brackets))

    def test_case06(self):
        s = Solution()
        s01 = Solution01()

        brackets = "(("
        self.assertEqual(False, s.isValid(brackets))
        self.assertEqual(False, s01.isValid(brackets))


if __name__ == '__main__':
    unittest.main()
