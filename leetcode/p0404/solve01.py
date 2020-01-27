class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, is_left: bool = False) -> int:
        if not root:
            return 0
        if is_left and not root.left:
            if root.right:
                return 0
            return root.val
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
