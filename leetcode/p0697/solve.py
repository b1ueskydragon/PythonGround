import math


# Degree of an Array
class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        if not nums:
            return 0
        table = {}
        for i, v in enumerate(nums):
            if v in table:
                table[v] += 1
            else:
                table[v] = 1
        max_freq = max(table.values())
        indices = {}
        for i, v in enumerate(nums):
            if table[v] == max_freq:
                if v not in indices:
                    indices[v] = [i]
                else:
                    indices[v] += [i]
        res = math.inf
        for v in indices.values():
            res = min(res, v[-1] - v[0] + 1)
        return res
