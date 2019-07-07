import unittest
from leetcode.p0008.solve import Solution


class MyAtoiTest(unittest.TestCase):
    def test_case01(self):
        a = Solution()
        target = "42"
        self.assertEqual(42, a.myAtoi(target))

    def test_case02(self):
        a = Solution()
        target = "   -42"
        self.assertEqual(-42, a.myAtoi(target))

    def test_case03(self):
        a = Solution()
        target = "4193 with words"
        self.assertEqual(4193, a.myAtoi(target))

    def test_case04(self):
        a = Solution()
        target = "words and 987"
        self.assertEqual(0, a.myAtoi(target))

    def test_case05(self):
        a = Solution()
        target = "-91283472332"
        self.assertEqual(-2147483648, a.myAtoi(target))

    def test_case06(self):
        a = Solution()
        target = "4-2"
        self.assertEqual(4, a.myAtoi(target))

    def test_case07(self):
        a = Solution()
        target = "-w"
        self.assertEqual(0, a.myAtoi(target))

    def test_case08(self):
        a = Solution()
        target = ""
        self.assertEqual(0, a.myAtoi(target))

    def test_case09(self):
        a = Solution()
        target = " "
        self.assertEqual(0, a.myAtoi(target))

    def test_case10(self):
        a = Solution()
        target = "+"
        self.assertEqual(0, a.myAtoi(target))


if __name__ == '__main__':
    unittest.main()
