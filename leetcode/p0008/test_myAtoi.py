import unittest
from leetcode.p0008.solve import Solution as A
from leetcode.p0008.solve01 import Solution as B


class MyAtoiTest(unittest.TestCase):
    def test_case01(self):
        a, b = A(), B()
        target = "42"
        self.assertEqual(42, a.myAtoi(target))
        self.assertEqual(42, b.myAtoi(target))

    def test_case02(self):
        a, b = A(), B()
        target = "   -42"
        self.assertEqual(-42, a.myAtoi(target))
        self.assertEqual(-42, b.myAtoi(target))

    def test_case03(self):
        a, b = A(), B()
        target = "4193 with words"
        self.assertEqual(4193, a.myAtoi(target))
        self.assertEqual(4193, b.myAtoi(target))

    def test_case04(self):
        a, b = A(), B()
        target = "words and 987"
        self.assertEqual(0, a.myAtoi(target))
        self.assertEqual(0, b.myAtoi(target))

    def test_case05(self):
        a, b = A(), B()
        target = "-91283472332"
        self.assertEqual(-2147483648, a.myAtoi(target))
        self.assertEqual(-2147483648, b.myAtoi(target))

    def test_case06(self):
        a, b = A(), B()
        target = "4-2"
        self.assertEqual(4, a.myAtoi(target))
        self.assertEqual(4, b.myAtoi(target))

    def test_case07(self):
        a, b = A(), B()
        target = "-w"
        self.assertEqual(0, a.myAtoi(target))
        self.assertEqual(0, b.myAtoi(target))

    def test_case08(self):
        a, b = A(), B()
        target = ""
        self.assertEqual(0, a.myAtoi(target))
        self.assertEqual(0, b.myAtoi(target))

    def test_case09(self):
        a, b = A(), B()
        target = " "
        self.assertEqual(0, a.myAtoi(target))
        self.assertEqual(0, b.myAtoi(target))

    def test_case10(self):
        a, b = A(), B()
        target = "+"
        self.assertEqual(0, a.myAtoi(target))
        self.assertEqual(0, b.myAtoi(target))


if __name__ == '__main__':
    unittest.main()
