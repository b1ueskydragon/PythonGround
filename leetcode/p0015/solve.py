class Solution:
    def threeSum_improve(self, nums):
        """
        sort -> binary search
        """
        n = len(nums)
        res = set()
        nums.sort()

        for i, x in enumerate(nums[:-2]):
            l = i + 1
            r = n - 1
            target = -x

            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((x, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return list(map(list, res))

    def threeSum(self, nums: [int]) -> [[int]]:
        """
        slow
        """
        res = set()
        n = len(nums)
        nums.sort()
        for i, x in enumerate(nums):
            for j in range(i + 1, n):
                y = nums[j]
                z = -(x + y)
                if z in set(nums[j + 1:]):
                    res.add((x, y, z))
        return list(map(list, res))
