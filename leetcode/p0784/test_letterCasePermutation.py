import unittest
from leetcode.p0784.solve import Solution as A
from leetcode.p0784.solve01 import Solution as B


class LetterCasePermutationTest(unittest.TestCase):
    def test_case01(self):
        a, b = A(), B()
        S = "a1b2"
        self.assertEqual(["A1B2", "A1b2", "a1B2", "a1b2"], a.letterCasePermutation(S))
        self.assertEqual(["a1b2", "A1b2", "A1B2", "a1B2"], b.letterCasePermutation(S))

    def test_case02(self):
        a, b = A(), B()
        S = "3z4"
        self.assertEqual(["3Z4", "3z4"], a.letterCasePermutation(S))
        self.assertEqual(["3z4", "3Z4"], b.letterCasePermutation(S))

    def test_from_upper(self):
        a, b = A(), B()
        S = "A"
        self.assertEqual(["A", "a"], a.letterCasePermutation(S))
        self.assertEqual(["A", "a"], b.letterCasePermutation(S))

    def test_only_alpha(self):
        a, b = A(), B()
        S = "abc"
        self.assertEqual(["ABC", "ABc", "AbC", "Abc", "aBC", "aBc", "abC", "abc"],
                         a.letterCasePermutation(S))
        self.assertEqual(["abc", "Abc", "ABc", "ABC", "AbC", "aBc", "aBC", "abC"], b.letterCasePermutation(S))

    def test_only_num(self):
        a, b = A(), B()
        S = "12345"
        self.assertEqual(["12345"], a.letterCasePermutation(S))
        self.assertEqual(["12345"], b.letterCasePermutation(S))


if __name__ == '__main__':
    unittest.main()
