class Solution:
    def threeSum_improve(self, nums):
        """
        sort -> binary search
        """
        n = len(nums)
        if n < 3:  # no more redundant calculation.
            return []
        res = set()
        nums.sort()

        for i, x in enumerate(nums[:-2]):
            """
            we can skip a turn that has same value as previous one
            since sorted first.
            """
            if i != 0 and x == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] == -x:
                    res.add((x, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > -x:
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
