"""
O(1) space

same as p0235/solve01.py
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # (root.val > p.val and root.val > q.val) or (root.val < p.val and root.val < q.val)
        while (root.val - p.val) * (root.val - q.val) > 0:
            # if p.val > root.val; root.val < p.val and root.val < q.val; lies left, else right
            root = (root.left, root.right)[p.val > root.val]
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

    # p=3, q=5
    print(s.lowestCommonAncestor(root, p=root.left.right.left, q=root.left.right.right).val)
