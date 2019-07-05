import unittest

from leetcode.p0860.solve import Solution as A
from leetcode.p0860.solve01 import Solution as B


class LemonadeChangeTest(unittest.TestCase):
    def test_case01(self):
        a, b = A(), B()
        bills = [5, 5, 5, 10, 20]
        self.assertEqual(True, a.lemonadeChange(bills))
        self.assertEqual(True, b.lemonadeChange(bills))

    def test_case02(self):
        a, b = A(), B()
        bills = [5, 5, 10]
        self.assertEqual(True, a.lemonadeChange(bills))
        self.assertEqual(True, b.lemonadeChange(bills))

    def test_case03(self):
        a, b = A(), B()
        bills = [10, 10]
        self.assertEqual(False, a.lemonadeChange(bills))
        self.assertEqual(False, b.lemonadeChange(bills))

    def test_case04(self):
        a, b = A(), B()
        bills = [5, 5, 10, 10, 20]
        self.assertEqual(False, a.lemonadeChange(bills))
        self.assertEqual(False, b.lemonadeChange(bills))

    def test_case05(self):
        a, b = A(), B()
        bills = [5, 5, 5, 5, 10, 5, 10, 10, 10, 20]
        self.assertEqual(True, a.lemonadeChange(bills))
        self.assertEqual(True, b.lemonadeChange(bills))

    def test_case06(self):
        a, b = A(), B()
        bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
        self.assertEqual(False, a.lemonadeChange(bills))
        self.assertEqual(False, b.lemonadeChange(bills))

    def test_case07(self):
        a, b = A(), B()
        bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5]
        self.assertEqual(False, a.lemonadeChange(bills))
        self.assertEqual(False, b.lemonadeChange(bills))


if __name__ == '__main__':
    unittest.main()
