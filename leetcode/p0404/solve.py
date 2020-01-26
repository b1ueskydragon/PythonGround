class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        q = deque([root])
        left_acc = 0
        while q:
            node = q.popleft()
            if node.left:
                left_acc += node.left.val
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return left_acc
