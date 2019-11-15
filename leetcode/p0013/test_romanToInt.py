import unittest

from leetcode.p0013.solve import Solution as A
from leetcode.p0013.solve01 import Solution as B


class RomanToIntTest(unittest.TestCase):
    def test_addition_only(self):
        a, b = A(), B()
        s = "LVIII"
        expected = 58
        self.assertEqual(expected, a.romanToInt(s))
        self.assertEqual(expected, b.romanToInt(s))

    def test_only_one_subtract(self):
        a, b = A(), B()
        s = "IV"
        expected = 4  # -1 + 5
        self.assertEqual(expected, a.romanToInt(s))
        self.assertEqual(expected, b.romanToInt(s))

    def test_complex_but_only_one_subtract(self):
        a, b = A(), B()
        s = "MCMXCIV"
        expected = 1994
        self.assertEqual(expected, a.romanToInt(s))
        self.assertEqual(expected, b.romanToInt(s))

    def test_one_more_subtracts(self):
        a, b = A(), B()
        s = "MMXLMDCIII"
        expected = 3543  # 1000 + 1000 - 10 - 50 + 1000 + 500 + 100 + 1  + 1 + 1
        self.assertEqual(expected, a.romanToInt(s))
        self.assertEqual(expected, b.romanToInt(s))
