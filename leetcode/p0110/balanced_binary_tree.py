class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.balanced = 1

    def isBalanced(self, root: TreeNode) -> bool:
        def max_depth(node) -> int:
            if not node:
                return 0
            lefts = max_depth(node.left) + 1
            rights = max_depth(node.right) + 1
            # print(node.val, lefts, rights)
            if abs(lefts - rights) > 1:
                self.balanced *= 0
            return max(lefts, rights)

        max_depth(root)
        return self.balanced != 0
