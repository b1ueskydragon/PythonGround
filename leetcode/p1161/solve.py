class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = [(root, 1)]
        max_val = (root.val, 1)  # or insert a sentinel
