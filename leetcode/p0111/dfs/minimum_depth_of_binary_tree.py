class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        def find(node, root, level):
            if not node and not root.left and not root.right:
                return level
            if not node:
                return float('inf')
            left = find(node.left, node, level + 1)
            right = find(node.right, node, level + 1)
            return min(left, right)

        return find(root, None, 0)
