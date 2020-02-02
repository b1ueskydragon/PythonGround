from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        parent = deque([(root, 1)])
        res = (root.val, 1)

        while parent:
            acc = 0
            children = deque()
            while parent:
                node, depth = parent.popleft()
                acc += node.val
                if node.left:
                    children.append((node.left, depth + 1))
                if node.right:
                    children.append((node.right, depth + 1))
                print(depth, acc, res[0])
                if acc > res[0]:
                    res = (acc, depth)
            parent = children  # next generation
        return res[1]
