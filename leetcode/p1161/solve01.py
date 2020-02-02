from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum = 0
        curr_depth = 1
        max_depth = 1
        parent = deque([root])

        while parent:
            # initialize before every new parent generated
            tmp = []
            curr_sum = 0

            for node in parent:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                curr_sum += node.val

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_depth = curr_depth

            curr_depth += 1

        return max_depth
