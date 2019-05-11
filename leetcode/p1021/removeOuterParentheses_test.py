import unittest
from leetcode.p1021.solve import Solution


class RemoveOuterParenthesesTest(unittest.TestCase):

    def test_remove_outer_parentheses_empty(self):
        s = Solution()

        pattern = ""
        expected = ""
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)

    def test_remove_outer_parentheses_remove_all(self):
        s = Solution()

        pattern = "()()"
        expected = ""
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)

    def test_remove_outer_parentheses_balanced_separated(self):
        s = Solution()

        pattern = "(()())(())"
        expected = "()()()"
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)

    def test_remove_outer_parentheses_balanced_nested_separated(self):
        s = Solution()

        pattern = "(()())(())(()(()))"
        expected = "()()()()(())"
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
