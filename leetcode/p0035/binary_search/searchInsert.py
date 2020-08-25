from typing import List


# Given a sorted array. No duplicates in the array.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l, r, m = 0, len(nums) - 1, 0
        while l <= r:
            m = l + (r - l) // 2
            mid = nums[m]
            if target == mid:
                return m
            elif target < mid:
                r = m - 1
            else:
                l = m + 1
        if target < nums[m]:
            return m
        else:
            return m + 1
