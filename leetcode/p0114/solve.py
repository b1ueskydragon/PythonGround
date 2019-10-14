# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Given a binary tree, flatten it to a linked list in-place.
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        if not root.left:
            return
        tmp = root.right
        root.right = root.left
        root.left = None
        self.flatten(root.right)
        while root.right:
            root = root.right
        else:
            root.right = tmp
