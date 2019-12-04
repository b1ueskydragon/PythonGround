class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None
        self.flag = True

    def _dfs(self, node):
        if node:
            self._dfs(node.left)
            if self.prev:
                self.flag &= self.prev.val < node.val
            self.prev = node
            self._dfs(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self._dfs(root)
        return self.flag

# Test cases
# [2, 1, 3]
# [5, 1, 4, null, null, 3, 6]
# [5, 1, 6, null, null, 7, 8]
# [10, null, 15, 6]
# [3, 1, 5, 0, 2, 4, 6]
