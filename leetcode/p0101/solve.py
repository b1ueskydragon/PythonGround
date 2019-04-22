"""
Iteratively
"""

from collections import deque
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # TODO reduce memory
        # TODO not solved yet
        queue = deque([root])
        stack = []

        while queue:
            cur = queue.popleft()
            if cur.left and cur.right:
                stack.append(cur.left.val)
                stack.append(cur.right.val)
                queue.append(cur.left)
                queue.append(cur.right)

        return True


if __name__ == '__main__':
    s = Solution()

    # [1, 2, 2, 3, 4, 4, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(s.isSymmetric(root=root))
