class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def is_valid(node):
        flag = True
        if node.left:
            flag &= node.left.val < node.val
        if node.right:
            flag &= node.val < node.right.val
        return flag

    @staticmethod
    def dfs(node):
        if node:
            return Solution.is_valid(node)
        # search left to right
        Solution.dfs(node.left)
        Solution.dfs(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        return Solution.dfs(root)

# Test cases
# [2, 1, 3]
# [5, 1, 4, null, null, 3, 6]
# [5, 1, 6, null, null, 7, 8]
# [10, null, 15, 6]
