from heapq import heapify, heappop


class Solution:
    # O(N logN)
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        xs = nums.copy()
        heapify(nums)
        i = 0
        order = dict()
        while nums:
            x = heappop(nums)
            if x not in order:
                order[x] = i
            i += 1
        return [order[x] for x in xs]
