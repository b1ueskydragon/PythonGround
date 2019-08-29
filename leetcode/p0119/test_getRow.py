import unittest

from leetcode.p0119.solve import Solution as A
from leetcode.p0119.solve01 import Solution as B


class RotateTest(unittest.TestCase):
    def test_getRow_0(self):
        a, b = A(), B()
        expected = [1]
        self.assertEqual(expected, a.getRow(0))
        self.assertEqual(expected, b.getRow(0))

    def test_getRow_1(self):
        a, b = A(), B()
        expected = [1, 1]
        self.assertEqual(expected, a.getRow(1))
        self.assertEqual(expected, b.getRow(1))

    def test_getRow_2(self):
        a, b = A(), B()
        expected = [1, 2, 1]
        self.assertEqual(expected, a.getRow(2))
        self.assertEqual(expected, b.getRow(2))

    def test_getRow_3(self):
        a, b = A(), B()
        expected = [1, 3, 3, 1]
        self.assertEqual(expected, a.getRow(3))
        self.assertEqual(expected, b.getRow(3))

    def test_getRow_4(self):
        a, b = A(), B()
        expected = [1, 4, 6, 4, 1]
        self.assertEqual(expected, a.getRow(4))
        self.assertEqual(expected, b.getRow(4))

    def test_getRow_5(self):
        a, b = A(), B()
        expected = [1, 5, 10, 10, 5, 1]
        self.assertEqual(expected, a.getRow(5))
        self.assertEqual(expected, b.getRow(5))

    def test_getRow_6(self):
        a, b = A(), B()
        expected = [1, 6, 15, 20, 15, 6, 1]
        self.assertEqual(expected, a.getRow(6))
        self.assertEqual(expected, b.getRow(6))

    def test_getRow_7(self):
        a, b = A(), B()
        expected = [1, 7, 21, 35, 35, 21, 7, 1]
        self.assertEqual(expected, a.getRow(7))
        self.assertEqual(expected, b.getRow(7))

    def test_getRow_30(self):
        a, b = A(), B()
        expected = [
            1, 30, 435, 4060, 27405, 142506, 593775, 2035800, 5852925,
            14307150, 30045015, 54627300, 86493225, 119759850, 145422675,
            155117520,
            145422675, 119759850, 86493225, 54627300, 30045015, 14307150,
            5852925, 2035800, 593775, 142506, 27405, 4060, 435, 30, 1
        ]
        self.assertEqual(expected, a.getRow(30))
        self.assertEqual(expected, b.getRow(30))
