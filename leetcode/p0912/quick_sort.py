class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        if not nums:
            return nums

        def quick_sort(left, right):
            pivot = nums[left + ((right - left + 1) // 2)]  # medium index counted from left index.
            l, r = left, right
            while l < r:
                while nums[l] < pivot:
                    l += 1
                while nums[r] > pivot:
                    r -= 1
                if l <= r:  # still pointers are not intersected.
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            if left < r:
                quick_sort(left, r)
            if l < right:
                quick_sort(l, right)

        quick_sort(0, len(nums) - 1)
        return nums
