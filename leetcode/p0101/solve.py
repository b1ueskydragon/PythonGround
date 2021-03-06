"""
Iteratively (queue)
"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque()
        queue.append(root)
        queue.append(root)  # additional space O(N) required

        while queue:
            # two nodes are extracted at Each time
            l = queue.popleft()
            r = queue.popleft()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            queue.append(l.left)
            queue.append(r.right)
            queue.append(l.right)
            queue.append(r.left)

        return True


if __name__ == '__main__':
    s = Solution()

    # [1, 2, 2, 3, 4, 4, 3]
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(2)
    a.left.left = TreeNode(3)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(4)
    a.right.right = TreeNode(3)

    print(s.isSymmetric(root=a))

    # [1, 2, 2, null, 3, null, 3]
    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(2)
    b.left.right = TreeNode(3)
    b.right.right = TreeNode(3)

    print(s.isSymmetric(root=b))
