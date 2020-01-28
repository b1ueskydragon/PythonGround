class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, is_left: bool = False) -> int:
        if not root:
            return 0
        return self.dfs([(root, False)], 0)

    def dfs(self, stack, acc):
        if not stack:
            return acc
        node, is_left = stack.pop()  # last in first out
        if not node:
            return self.dfs(stack, acc)
        if is_left and not node.left and not node.right:
            return self.dfs(stack, acc + node.val)
        else:
            stack.append((node.left, True))
            stack.append((node.right, False))
            return self.dfs(stack, acc)
