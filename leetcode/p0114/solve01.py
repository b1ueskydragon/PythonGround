# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None  # back-up previous result for append next

    def flatten(self, root: TreeNode) -> None:
        """
        Given a binary tree, flatten it to a linked list in-place.
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)  # left should be preceded by right
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
