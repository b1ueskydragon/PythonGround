import unittest

from leetcode.p0297.solve import *


class CodecTest(unittest.TestCase):
    def test_serialize_a_tree_inclined_right_side(self):
        codec = Codec()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        serialized = codec.serialize(root)
        self.assertEqual(
            "[1, 2, 3, null, null, 4, 5, null, null, null, null]",
            serialized)

    def test_serialize_a_tree_has_a_odd_leaf(self):
        codec = Codec()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(6)
        serialized = codec.serialize(root)
        self.assertEqual(
            "[1, 2, 3, null, null, 4, 5, null, null, null, 6, null, null]",
            serialized)

    def test_deserialize_a_tree_inclined_right_side(self):
        codec = Codec()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        deserialized = codec.deserialize(codec.serialize(root))

        self.assertEqual(root.val, deserialized.val)
        self.assertEqual(root.left.val, deserialized.left.val)
        self.assertEqual(root.right.val, deserialized.right.val)

        # None
        self.assertEqual(root.left.left, deserialized.left.left)
        # None
        self.assertEqual(root.left.right, deserialized.left.right)

        self.assertEqual(root.right.left.val, deserialized.right.left.val)
        self.assertEqual(root.right.right.val, deserialized.right.right.val)
