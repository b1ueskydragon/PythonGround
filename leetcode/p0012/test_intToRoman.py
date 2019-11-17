import unittest

from leetcode.p0012.solve import Solution as A


class IntToRomanTest(unittest.TestCase):
    def test_addition_only(self):
        a = A()
        num = 58
        expected = "LVIII"
        self.assertEqual(expected, a.intToRoman(num))

    def test_only_one_subtract(self):
        a = A()
        num = 4
        expected = "IV"
        self.assertEqual(expected, a.intToRoman(num))

    def test_complex_but_only_one_subtract(self):
        a = A()
        num = 1994
        expected = "MCMXCIV"
        self.assertEqual(expected, a.intToRoman(num))

    def test_one_more_subtracts(self):
        a = A()
        num = 3543
        expected = "MMXLMDCIII"
        self.assertEqual(expected, a.intToRoman(num))
