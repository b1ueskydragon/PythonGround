"""
It doesn't matter what you leave beyond the returned length,
what values are set beyond the returned length.
"""


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        """
        :param nums: sorted array
        :return: length to retrieve
        """
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
            nums[i] = nums[j]
            j += 1
        return i + 1
