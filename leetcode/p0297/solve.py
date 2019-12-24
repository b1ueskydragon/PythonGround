from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = deque()
        q.append(root)
        while q:
            parent = q.popleft()
            if parent:
                res.append(parent.val)
                # add children
                # child be the next parent
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
        # TODO insert None if node is none
        # TODO mkStr
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # TODO
        return None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# TODO move to spec
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
serialized = codec.serialize(root)
print(serialized)
