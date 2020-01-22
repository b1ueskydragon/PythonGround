import math
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        q = deque([root])
        mapping = []
        while q:
            parent = q.popleft()
            x = 0
            if parent:
                x = parent.val
                q.append(parent.left)
                q.append(parent.right)
            mapping.append((level, x))
            level += 1
        # print(mapping)
        r = deque(mapping)
        max_sum, tmp = (0, -2147483648), 0
        table = {1, 2, 4, 8}
        start, end = 1, 2
        while r:
            while start < end:
                if not r:
                    break
                l, v = r.popleft()
                tmp += v
                start += 1
            else:
                if max_sum[1] < tmp:
                    max_sum = (int(math.log2(end)), tmp)
                tmp = 0
                start = end
                end <<= 1
        return max_sum[0]
