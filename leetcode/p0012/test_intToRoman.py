import unittest

from leetcode.p0012.solve import Solution as A


class IntToRomanTest(unittest.TestCase):
    def test_01(self):
        a = A()
        num = 58
        expected = "LVIII"
        self.assertEqual(expected, a.intToRoman(num))

    def test_02(self):
        a = A()
        num = 4
        expected = "IV"
        self.assertEqual(expected, a.intToRoman(num))

    def test_03(self):
        a = A()
        num = 1994
        expected = "MCMXCIV"
        self.assertEqual(expected, a.intToRoman(num))

    def test_04(self):
        a = A()
        num = 3543
        expected = "MMMDXLIII"
        self.assertEqual(expected, a.intToRoman(num))

    def test_05(self):
        a = A()
        num = 2222
        expected = "MMCCXXII"
        self.assertEqual(expected, a.intToRoman(num))
