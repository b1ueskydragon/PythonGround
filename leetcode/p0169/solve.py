"""
The array is non-empty and the majority element always exist in the array.
"""


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        size = len(nums) // 2
        count = dict()
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
            if count[x] > size: return x
