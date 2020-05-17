from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        if not root:
            return []
        res = []
        q = deque([root])
        size = 1
        while q:
            val = None
            for _ in range(size):  # retrieve based on the size of the stair.
                parent = q.popleft()
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
                val = parent.val
            res.append(val)  # overwrite; the most recently retrieved val in the stair.
            size = len(q)
        return res
