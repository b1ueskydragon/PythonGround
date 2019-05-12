import unittest
from leetcode.p1021.solve import Solution
from leetcode.p1021.solve01 import Solution as Solution01


class RemoveOuterParenthesesTest(unittest.TestCase):
    s = Solution()
    s01 = Solution01()

    def test_remove_outer_parentheses_empty(self):
        pattern = ""
        expected = ""

        actual = self.s.removeOuterParentheses(pattern)
        actual01 = self.s01.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual01)

    def test_remove_outer_parentheses_remove_all(self):
        pattern = "()()"
        expected = ""

        actual = self.s.removeOuterParentheses(pattern)
        actual01 = self.s01.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual01)

    def test_remove_outer_parentheses_balanced_separated(self):
        pattern = "(()())(())"
        expected = "()()()"

        actual = self.s.removeOuterParentheses(pattern)
        actual01 = self.s01.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual01)

    def test_remove_outer_parentheses_balanced_nested_separated(self):
        pattern = "(()())(())(()(()))"
        expected = "()()()()(())"

        actual = self.s.removeOuterParentheses(pattern)
        actual01 = self.s01.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual01)


if __name__ == '__main__':
    unittest.main()
