import unittest

from leetcode.p1021.solve import Solution


class RemoveOuterParenthesesTest(unittest.TestCase):

    def remove_outer_parentheses_empty(self):
        s = Solution()

        pattern = ""
        expected = pattern
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)

    def remove_outer_parentheses_balanced_closed_separated(self):
        s = Solution()

        pattern = "(()(()))"
        expected = pattern
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)

    def remove_outer_parentheses_only_open(self):
        s = Solution()

        pattern = "((("
        expected = 3
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)

    def remove_outer_parentheses_only_closed(self):
        s = Solution()

        pattern = "))"
        expected = 2
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)

    def remove_outer_parentheses_closed_first(self):
        s = Solution()

        pattern = ")))(()"
        expected = 4
        actual = s.removeOuterParentheses(pattern)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
