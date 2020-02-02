import unittest

from leetcode.p1161.solve import Solution as A
from leetcode.p1161.solve import TreeNode


class MaxLevelSumTest(unittest.TestCase):
    def test_basic_balanced_leaf(self):
        a = A()
        # [3,1,4]
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        self.assertEqual(2, a.maxLevelSum(root))

    def test_not_a_balanced_leaf(self):
        a = A()
        root = TreeNode(99)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)

        root.left.left.right = TreeNode(100)

        self.assertEqual(4, a.maxLevelSum(root))

    def test_sample(self):
        a = A()
        # [1,7,0,7,-8,null,null]
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)
        self.assertEqual(2, a.maxLevelSum(root))

    def test_negate_values(self):
        # so, the init max_sum[1] should not be set zero.
        a = A()
        # [-1111, -99, 3, null, -1005]
        root = TreeNode(-1111)
        root.left = TreeNode(-99)
        root.right = TreeNode(3)
        root.left.right = TreeNode(-1005)
        self.assertEqual(2, a.maxLevelSum(root))

    def test_tree_has_a_complex_children_structure(self):
        #  [1,2,3,null,4,5,6,null,null,7,8,9,10,11,null,12]
        a = A()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        root.right.left.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.right.left = TreeNode(9)
        root.right.right.right = TreeNode(10)
        root.right.left.left.left = TreeNode(11)
        root.right.left.right.left = TreeNode(12)
        self.assertEqual(4, a.maxLevelSum(root))
