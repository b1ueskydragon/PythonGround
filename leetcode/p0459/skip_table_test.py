import unittest
from leetcode.p0459.solve01 import Solution


class SkipTableTest(unittest.TestCase):
    def test01(self):
        s = Solution()
        pattern = 'ababc'
        self.assertEqual([0, 0, 1, 2, 0], s.skip_table(pattern))

    def test02(self):
        s = Solution()
        pattern = 'aabaaac'
        self.assertEqual([0, 1, 0, 1, 2, 2, 0], s.skip_table(pattern))

    def test03(self):
        s = Solution()
        pattern = 'aabaaab'
        self.assertEqual([0, 1, 0, 1, 2, 2, 3], s.skip_table(pattern))

    def test04(self):
        s = Solution()
        pattern = 'ababba'
        self.assertEqual([0, 0, 1, 2, 0, 1], s.skip_table(pattern))
