from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        left_acc = 0
        if root:
            q = deque([root])
            while q:
                node = q.popleft()
                if node.left:
                    if not node.left.left and not node.left.right:
                        left_acc += node.left.val
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return left_acc
