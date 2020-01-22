from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        q = deque([root])
        res = []
        while q:
            parent = q.popleft()
            x = 0
            if parent:
                x = parent.val
                q.append(parent.left)
                q.append(parent.right)
            res.append({level: x})
            level += 1
        print(res)
        # TODO
