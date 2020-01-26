import unittest

from leetcode.p0404.solve import TreeNode, Solution as A


class SumOfLeftLeavesTest(unittest.TestCase):
    def test_large(self):
        # [3, 9, 20, null, null, 15, 7]
        a = A()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(24, a.sumOfLeftLeaves(root))

    # TODO :
    #  pass the case
    #  [1,2,3,null,4,5,6,null,null,7,8,9,10,11,null,12]


if __name__ == '__main__':
    unittest.main()
