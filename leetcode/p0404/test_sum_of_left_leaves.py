import unittest

from leetcode.p0404.solve import TreeNode, Solution as A
from leetcode.p0404.solve01 import Solution as B
from leetcode.p0404.solve0101 import Solution as C


class SumOfLeftLeavesTest(unittest.TestCase):
    def test_sample(self):
        # [3,9,20,null,null,15,7]
        a = A()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(24, a.sumOfLeftLeaves(root))

    def test_empty(self):
        # []
        a = A()
        self.assertEqual(0, a.sumOfLeftLeaves(None))

    def test_get_only_leaves_have_not_children(self):
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
        root.right.right.left = TreeNode(9)  # acc
        root.right.right.right = TreeNode(10)
        root.right.left.left.left = TreeNode(11)  # acc
        root.right.left.right.left = TreeNode(12)  # acc
        self.assertEqual(32, a.sumOfLeftLeaves(root))

    def test_single_element(self):
        a = A()
        root = TreeNode(1)
        self.assertEqual(0, a.sumOfLeftLeaves(root))

    def test_zigzag(self):
        #  [5,null,6,7,null,null,8,9]
        a = A()
        root = TreeNode(5)
        root.right = TreeNode(6)
        root.right.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.left.right.left = TreeNode(9)

        self.assertEqual(9, a.sumOfLeftLeaves(root))

    def test_sample_DFS(self):
        # [3,9,20,null,null,15,7]
        b = B()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(24, b.sumOfLeftLeaves(root))

    def test_empty_DFS(self):
        # []
        b = B()
        self.assertEqual(0, b.sumOfLeftLeaves(None))

    def test_single_element_DFS(self):
        b = B()
        root = TreeNode(1)
        self.assertEqual(0, b.sumOfLeftLeaves(root))

    def test_get_only_leaves_have_not_children_DFS(self):
        #  [1,2,3,null,4,5,6,null,null,7,8,9,10,11,null,12]
        b = B()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        root.right.left.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.right.left = TreeNode(9)  # acc
        root.right.right.right = TreeNode(10)
        root.right.left.left.left = TreeNode(11)  # acc
        root.right.left.right.left = TreeNode(12)  # acc
        self.assertEqual(32, b.sumOfLeftLeaves(root))

    def test_zigzag_DFS(self):
        #  [5,null,6,7,null,null,8,9]
        b = B()
        root = TreeNode(5)
        root.right = TreeNode(6)
        root.right.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.left.right.left = TreeNode(9)

        self.assertEqual(9, b.sumOfLeftLeaves(root))

    def test_sample_DFS_tailrec(self):
        c = C()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(24, c.sumOfLeftLeaves(root))

    def test_empty_DFS_tailrec(self):
        # []
        c = C()
        self.assertEqual(0, c.sumOfLeftLeaves(None))

    def test_single_element_DFS_tailrec(self):
        c = C()
        root = TreeNode(1)
        self.assertEqual(0, c.sumOfLeftLeaves(root))

    def test_get_only_leaves_have_not_children_DFS_tailrec(self):
        #  [1,2,3,null,4,5,6,null,null,7,8,9,10,11,null,12]
        c = C()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        root.right.left.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.right.left = TreeNode(9)  # acc
        root.right.right.right = TreeNode(10)
        root.right.left.left.left = TreeNode(11)  # acc
        root.right.left.right.left = TreeNode(12)  # acc
        self.assertEqual(32, c.sumOfLeftLeaves(root))

    def test_zigzag_DFS_tailrec(self):
        #  [5,null,6,7,null,null,8,9]
        c = C()
        root = TreeNode(5)
        root.right = TreeNode(6)
        root.right.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.left.right.left = TreeNode(9)

        self.assertEqual(9, c.sumOfLeftLeaves(root))


if __name__ == '__main__':
    unittest.main()
