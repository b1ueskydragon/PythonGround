import math


# Degree of an Array
class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        distance = {}  # v -> distance
        count = {}  # v -> frequency
        start = {}  # v -> the first appearance point
        for i, v in enumerate(nums):
            if v in start:
                distance[v] = i - start[v] + 1
                count[v] += 1
            else:
                distance[v] = 1
                start[v] = i
                count[v] = 1

        max_freq = max(count.values())
        res = math.inf

        for v in distance.keys():
            if count[v] == max_freq:
                res = min(res, distance[v])
        return res
