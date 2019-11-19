import unittest

from leetcode.p0872.solve import Solution as A
from leetcode.p0872.solve import TreeNode as Node


class LeafSimilarTest(unittest.TestCase):
    def test_same_order_diff_depth(self):
        a = A()

        # [3,5,1,6,2,9,8,null,null,7,4]
        root1 = Node(3)
        root1.left = Node(5)
        root1.right = Node(1)
        root1.left.left = Node(6)
        root1.left.right = Node(2)
        root1.right.left = Node(9)
        root1.right.right = Node(8)
        root1.left.right.left = Node(7)
        root1.left.right.right = Node(4)

        # [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
        root2 = Node(3)
        root2.left = Node(5)
        root2.right = Node(1)
        root2.left.left = Node(6)
        root2.left.right = Node(7)
        root2.right.left = Node(4)
        root2.right.right = Node(2)
        root2.right.right.left = Node(9)
        root2.right.right.right = Node(8)

        self.assertTrue(a.leafSimilar(root1, root2))

    def test_diff_order_diff_depth(self):
        a = A()

        # [1,null,2,null,3,null,6,5,4]
        root1 = Node(1)
        root1.right = Node(2)
        root1.right.right = Node(3)
        root1.right.right.right = Node(6)
        root1.right.right.right.left = Node(5)
        root1.right.right.right.right = Node(4)

        # [1,2,null,3,6,null,4,null,5]
        root2 = Node(1)
        root2.left = Node(2)
        root2.left.left = Node(3)
        root2.left.right = Node(6)
        root2.left.left.right = Node(4)
        root2.left.right.right = Node(5)

        self.assertFalse(a.leafSimilar(root1, root2))

    def test_linear_tree_diff_direction_same_depth(self):
        a = A()

        # [1,null,2,null,3,null,4]
        root1 = Node(1)
        root1.right = Node(2)
        root1.right.right = Node(3)
        root1.right.right.right = Node(4)

        # [1,2,null,3,null,4]
        root2 = Node(1)
        root2.left = Node(2)
        root2.left.left = Node(3)
        root2.left.left.left = Node(4)
        self.assertTrue(a.leafSimilar(root1, root2))

    def test_diff_order_same_depth(self):
        a = A()

        # [44,79,25,null,null,112,7,74,49,2,122]
        root1 = Node(44)
        root1.left = Node(79)
        root1.right = Node(25)
        root1.right.left = Node(112)
        root1.right.right = Node(7)
        root1.right.left.left = Node(74)
        root1.right.left.right = Node(49)
        root1.right.right.left = Node(2)
        root1.right.right.right = Node(122)

        # [38,86,120,49,54,2,122,null,null,74,79]
        root2 = Node(38)
        root2.left = Node(86)
        root2.right = Node(120)
        root2.left.left = Node(49)
        root2.left.right = Node(54)
        root2.right.left = Node(2)
        root2.right.right = Node(122)
        root2.left.right.left = Node(74)
        root2.left.right.right = Node(79)

        self.assertFalse(a.leafSimilar(root1, root2))
