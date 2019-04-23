"""
Recursively

O(N) space at worst (if tree is linear o-o-o- ...)
O(N) time (retrieval all N nodes once)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self._yes(root, root)

    def _yes(self, left, right):
        if not left and not right:  # empty is symmetric
            return True
        if not left or not right:  # only one side exists (not symmetric)
            return False

        return \
            left.val == right.val \
            and self._yes(left.right, right.left) \
            and self._yes(left.left, right.right)


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
