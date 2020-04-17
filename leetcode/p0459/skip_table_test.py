import unittest
from leetcode.p0459.solve01 import Solution


class SkipTableTest(unittest.TestCase):
    def test01(self):
        s = Solution()
        pattern = 'ababc'
        self.assertEqual([0, 0, 1, 2, 0], s.skip_table(pattern))
