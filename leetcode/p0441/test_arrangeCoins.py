import unittest

from leetcode.p0441.solve import Solution as A
from leetcode.p0441.solve01 import Solution as B
from leetcode.p0441.solve02 import Solution as C


class ArrangeCoinsTest(unittest.TestCase):
    def test_5(self):
        a, b, c = A(), B(), C()
        self.assertEqual(2, a.arrangeCoins(5))
        self.assertEqual(2, a.arrangeCoins_(5))
        self.assertEqual(2, b.arrangeCoins(5))
        self.assertEqual(2, b.arrangeCoins_(5))
        self.assertEqual(2, c.arrangeCoins(5))

    def test_6(self):
        a, b, c = A(), B(), C()
        self.assertEqual(3, a.arrangeCoins(6))
        self.assertEqual(3, a.arrangeCoins_(6))
        self.assertEqual(3, b.arrangeCoins(6))
        self.assertEqual(3, b.arrangeCoins_(6))
        self.assertEqual(3, c.arrangeCoins(6))

    def test_8(self):
        a, b, c = A(), B(), C()
        self.assertEqual(3, a.arrangeCoins(8))
        self.assertEqual(3, a.arrangeCoins_(8))
        self.assertEqual(3, b.arrangeCoins(8))
        self.assertEqual(3, b.arrangeCoins_(8))
        self.assertEqual(3, c.arrangeCoins(8))


if __name__ == '__main__':
    unittest.main()
