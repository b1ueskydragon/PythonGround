import unittest
from leetcode.p0860.solve import Solution


class LemonadeChangeTest(unittest.TestCase):
    def test_case01(self):
        s = Solution()
        bills = [5, 5, 5, 10, 20]
        self.assertEqual(True, s.lemonadeChange(bills))

    def test_case02(self):
        s = Solution()
        bills = [5, 5, 10]
        self.assertEqual(True, s.lemonadeChange(bills))

    def test_case03(self):
        s = Solution()
        bills = [10, 10]
        self.assertEqual(False, s.lemonadeChange(bills))

    def test_case04(self):
        s = Solution()
        bills = [5, 5, 10, 10, 20]
        self.assertEqual(False, s.lemonadeChange(bills))

    def test_case05(self):
        s = Solution()
        bills = [5, 5, 5, 5, 10, 5, 10, 10, 10, 20]
        self.assertEqual(True, s.lemonadeChange(bills))

    def test_case06(self):
        s = Solution()
        bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
        self.assertEqual(False, s.lemonadeChange(bills))

    def test_case07(self):
        s = Solution()
        bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5]
        self.assertEqual(False, s.lemonadeChange(bills))


if __name__ == '__main__':
    unittest.main()
