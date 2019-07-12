import unittest
from leetcode.p0441.solve import Solution as A


class ArrangeCoinsTest(unittest.TestCase):
    def test_5(self):
        a = A()
        self.assertEqual(2, a.arrangeCoins(5))
        self.assertEqual(2, a.arrangeCoins_(5))

    def test_6(self):
        a = A()
        self.assertEqual(3, a.arrangeCoins(6))
        self.assertEqual(3, a.arrangeCoins_(6))

    def test_8(self):
        a = A()
        self.assertEqual(3, a.arrangeCoins(8))
        self.assertEqual(3, a.arrangeCoins_(8))


if __name__ == '__main__':
    unittest.main()
