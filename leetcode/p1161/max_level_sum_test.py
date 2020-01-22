import unittest

from leetcode.p1161.solve import Solution as A
from leetcode.p1161.solve import TreeNode


class MaxLevelSumTest(unittest.TestCase):
    def test_basic(self):
        a = A()
        # [3,1,4]
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        self.assertEqual(2, a.maxLevelSum(root))

    def test_sample(self):
        a = A()
        # [1,7,0,7,-8,null,null]
        root = TreeNode(1)
        # TODO
        self.assertEqual(2, a.maxLevelSum(root))
