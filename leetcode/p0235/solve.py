"""
Binary `Search` Tree

O(N) time at worse,
O(N) space by the using recursion stack.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root

        if root.val > p.val and root.val > q.val:  # lies in left (standard case)
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:  # lies in right (standard case)
            return self.lowestCommonAncestor(root.right, p, q)

        return root


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    s = Solution()

    # p=7, q=8
    print(s.lowestCommonAncestor(root, p=root.right.left, q=root.right).val)
