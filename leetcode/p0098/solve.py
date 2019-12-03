class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.flag = True

    def is_valid(self, node):
        if node.left:
            self.flag &= node.left.val < node.val
        if node.right:
            self.flag &= node.val < node.right.val

    def dfs(self, node):
        if node:
            self.dfs(node.left)
            self.is_valid(node)
            self.dfs(node.right)
            self.is_valid(node)

    def isValidBST(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.flag

# Test cases
# [2, 1, 3]
# [5, 1, 4, null, null, 3, 6]
# [5, 1, 6, null, null, 7, 8]
# [10, null, 15, 6]
