"""
Iteratively (stack)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root, root]

        while stack:
            r = stack.pop()
            l = stack.pop()

            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False

            stack.append(r.right)
            stack.append(l.left)
            stack.append(r.left)
            stack.append(l.right)

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
