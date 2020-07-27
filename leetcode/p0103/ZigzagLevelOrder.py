from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def find(q, res, size, vector):
            while q:
                for _ in range(size):
                    parent = q.popleft()
                    if parent.right:
                        q.append(parent.right)
                    if parent.left:
                        q.append(parent.left)
                size = len(q)
                if q:
                    children = [node.val for node in q]
                    if vector == 1:
                        res.append(children)
                    else:
                        res.append(reversed(children))
                vector *= -1
            return res

        return find(deque([root]), [[root.val]], 1, 1)
