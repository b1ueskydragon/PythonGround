from collections import deque as q
from leetcode.p0872.TreeNode import TreeNode


class Solution:
    res = q()
    is_same = True

    def _dfs(self, root):
        if root.left:
            self._dfs(root.left)
        if root.right:
            self._dfs(root.right)
        if not root.left and not root.right:
            self.res.append(root.val)

    def _dfs_with_pop(self, root):
        if root.left:
            self._dfs_with_pop(root.left)
        if root.right:
            self._dfs_with_pop(root.right)
        if not root.left and not root.right:
            self.is_same &= (root.val == self.res.popleft())

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self._dfs(root1)
        self._dfs_with_pop(root2)
        return self.is_same
