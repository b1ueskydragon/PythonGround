"""
use deque, since it provides pop or append both end efficiently.
"""


class Solution:
    def getRow(self, rowIndex):
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        return self.pascal(self.getRow(rowIndex - 1), rowIndex)

    def pascal(self, prev_res, k):
        from collections import deque
        queue = deque(prev_res)
        acc = 0
        while k:
            curr = queue.popleft()
            queue.append(acc + curr)
            acc = curr
            k -= 1
        queue.append(1)
        return list(queue)
