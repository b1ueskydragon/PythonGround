import unittest

from leetcode.p0119.solve import Solution as A


class RotateTest(unittest.TestCase):
    def test_getRow_0(self):
        a = A()
        expected = [1]
        self.assertEqual(expected, a.getRow(0))

    def test_getRow_1(self):
        a = A()
        expected = [1, 1]
        self.assertEqual(expected, a.getRow(1))

    def test_getRow_2(self):
        a = A()
        expected = [1, 2, 1]
        self.assertEqual(expected, a.getRow(2))

    def test_getRow_3(self):
        a = A()
        expected = [1, 3, 3, 1]
        self.assertEqual(expected, a.getRow(3))

    def test_getRow_4(self):
        a = A()
        expected = [1, 4, 6, 4, 1]
        self.assertEqual(expected, a.getRow(4))

    def test_getRow_5(self):
        a = A()
        expected = [1, 5, 10, 10, 5, 1]
        self.assertEqual(expected, a.getRow(5))
