import unittest

from leetcode.p0404.solve import TreeNode, Solution as A


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


if __name__ == '__main__':
    unittest.main()
