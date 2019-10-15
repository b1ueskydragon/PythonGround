import unittest
from leetcode.p0114.solve import TreeNode
from leetcode.p0114.solve import Solution as A
from leetcode.p0114.solve01 import Solution as B


class FlattenBinaryTreeToLinkedListTest(unittest.TestCase):
    def test_flatten(self):
        a = A()
        # root = [1, 2, 5, 3, 4, None, 6]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)

        a.flatten(root)

        # root = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
        self.assertEqual(1, root.val)
        self.assertEqual(2, root.right.val)
        self.assertEqual(3, root.right.right.val)
        self.assertEqual(4, root.right.right.right.val)
        self.assertEqual(5, root.right.right.right.right.val)
        self.assertEqual(6, root.right.right.right.right.right.val)

    def test_flatten_B(self):
        b = B()
        # root = [1, 2, 5, 3, 4, None, 6]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)

        b.flatten(root)

        # root = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
        self.assertEqual(1, root.val)
        self.assertEqual(2, root.right.val)
        self.assertEqual(3, root.right.right.val)
        self.assertEqual(4, root.right.right.right.val)
        self.assertEqual(5, root.right.right.right.right.val)
        self.assertEqual(6, root.right.right.right.right.right.val)

    def test_empty_root(self):
        a = A()
        root = None
        a.flatten(root)
        self.assertEqual(None, root)

    def test_empty_root_B(self):
        b = B()
        root = None
        b.flatten(root)
        self.assertEqual(None, root)

    def test_has_left_to_search(self):
        a = A()
        # root = [1, None, 2, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        a.flatten(root)

        # root = [1, None, 2, None, 3]
        self.assertEqual(1, root.val)
        self.assertEqual(2, root.right.val)
        self.assertEqual(3, root.right.right.val)

    def test_has_left_to_search_B(self):
        b = B()
        # root = [1, None, 2, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        b.flatten(root)

        # root = [1, None, 2, None, 3]
        self.assertEqual(1, root.val)
        self.assertEqual(2, root.right.val)
        self.assertEqual(3, root.right.right.val)


if __name__ == '__main__':
    unittest.main()
