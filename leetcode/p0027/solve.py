"""
O(N) Time O(1) Space
"""


class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]  # replace anyway even nums[n-1] is the val.
                n -= 1  # reduce the range to retrieval afterward.
            else:
                i += 1  # only go ahead if nums[i] is not the val.
        return n
