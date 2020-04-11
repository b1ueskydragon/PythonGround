class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        def quick_sort(left, right):
            pivot = nums[(right - left + 1) / 2] # ???
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


print(Solution().sortArray([50000, 0, -50000, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1]))
