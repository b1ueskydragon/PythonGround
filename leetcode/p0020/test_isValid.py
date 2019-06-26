import unittest

from leetcode.p0020.solve import Solution


class IsValidTest(unittest.TestCase):
    def test_empty(self):
        s = Solution()
        brackets = ""
        self.assertEqual(True, s.isValid(brackets))

    def test_case01(self):
        s = Solution()
        brackets = "()"
        self.assertEqual(True, s.isValid(brackets))

    def test_case02(self):
        s = Solution()
        brackets = "()[]{}"
        self.assertEqual(True, s.isValid(brackets))

    def test_case03(self):
        s = Solution()
        brackets = "(]"
        self.assertEqual(False, s.isValid(brackets))

    def test_case04(self):
        s = Solution()
        brackets = "([)]"
        self.assertEqual(False, s.isValid(brackets))

    def test_case05(self):
        s = Solution()
        brackets = "{[]}"
        self.assertEqual(True, s.isValid(brackets))


if __name__ == '__main__':
    unittest.main()
