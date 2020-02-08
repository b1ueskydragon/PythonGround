from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = root.val  # not 0 for a single node tree
        max_depth = 1
        curr_depth = 1
        seed = deque([root])
        while seed:
            # initialize before every new parent generated
            curr = []
            curr_sum = 0

            for node in seed:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
                curr_sum += node.val

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_depth = curr_depth

            curr_depth += 1
            seed = curr
        return max_depth
