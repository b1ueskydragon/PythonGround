class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        j = i - 1
        the_largest = False
        while nums[j] >= nums[i] and j > 0:
            j -= 1
            i -= 1
            the_largest = (j == 0 and nums[j] >= nums[i])

        left, right = j, len(nums) - 1
        if not the_largest:
            swap = i
            while i < len(nums):
                if nums[j] < nums[i] <= nums[swap]:  # swap to the rightmost index if equals.
                    swap = i
                i += 1
            nums[j], nums[swap] = nums[swap], nums[j]
            left += 1

        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
