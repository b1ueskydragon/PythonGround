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
            "[1, 2, 3, null, null, 4, 5]",
            serialized)

    def test_serialize_a_tree_has_a_odd_leaf_right(self):
        codec = Codec()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(6)
        serialized = codec.serialize(root)
        self.assertEqual(
            "[1, 2, 3, null, null, 4, 5, null, null, null, 6]",
            serialized)

    def test_serialize_a_tree_has_a_odd_leaf_left(self):
        codec = Codec()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.right.left = TreeNode(6)
        serialized = codec.serialize(root)
        self.assertEqual(
            "[1, 2, 3, null, null, 4, 5, null, null, 6, null]",
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
        self.assertEqual(root.right.left.val, deserialized.right.left.val)
        self.assertEqual(root.right.right.val, deserialized.right.right.val)

        self.assertIsNone(root.left.left)
        self.assertIsNone(deserialized.left.left)
        self.assertIsNone(root.left.right)
        self.assertIsNone(deserialized.left.right)

    def test_deserialize_a_tree_all_have_a_node(self):
        codec = Codec()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        deserialized = codec.deserialize(codec.serialize(root))

        self.assertEqual(root.val, deserialized.val)
        self.assertEqual(root.left.val, deserialized.left.val)
        self.assertEqual(root.right.val, deserialized.right.val)
        self.assertEqual(root.left.left.val, deserialized.left.left.val)
        self.assertEqual(root.left.right.val, deserialized.left.right.val)
        self.assertEqual(root.right.left.val, deserialized.right.left.val)
        self.assertEqual(root.right.right.val, deserialized.right.right.val)

    def test_deserialize_empty(self):
        codec = Codec()
        deserialized = codec.deserialize(codec.serialize(None))
        self.assertEqual([], deserialized)  # not a [None]

    def test_deserialize_includes_numeric_zero(self):
        codec = Codec()
        root = TreeNode(-1)
        root.left = TreeNode(0)  # 0 != None
        root.right = TreeNode(1)
        deserialized = codec.deserialize(codec.serialize(root))

        self.assertEqual(root.val, deserialized.val)
        self.assertEqual(root.left.val, deserialized.left.val)
        self.assertEqual(root.right.val, deserialized.right.val)
