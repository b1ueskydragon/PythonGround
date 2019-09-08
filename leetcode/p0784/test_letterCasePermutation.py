import unittest
from leetcode.p0784.solve import Solution as A


class LetterCasePermutationTest(unittest.TestCase):
    def test_case01(self):
        a = A()
        S = "a1b2"
        expected = ["A1B2", "A1b2", "a1B2", "a1b2"]
        self.assertEqual(expected, a.letterCasePermutation(S))

    def test_case02(self):
        a = A()
        S = "3z4"
        expected = ["3Z4", "3z4"]
        self.assertEqual(expected, a.letterCasePermutation(S))

    def test_case03(self):
        a = A()
        S = "12345"
        expected = ["12345"]
        self.assertEqual(expected, a.letterCasePermutation(S))


if __name__ == '__main__':
    unittest.main()
