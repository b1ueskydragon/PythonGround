from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# find the nearest leaf node from the root.
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        children = deque([root])
        stair = 1
        stair_size = 1
        while children:
            for _ in range(stair_size):
                parent = children.popleft()
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            if children:
                stair += 1
            for child in children:
                if not child.left and not child.right:
                    return stair
            stair_size = len(children)
        return stair
