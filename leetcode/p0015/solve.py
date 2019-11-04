class Solution:
    def twoSum(self, nums):
        """
        x  = a + b
        -x = c
        """
        res = []
        pairs = {}  # -x -> x
        # triplets = {}
        for i, x in enumerate(nums):
            if -x in pairs:
                res.append([pairs[-x], -x])
            else:
                pairs[x] = -x
        return res

    def threeSum(self, nums: [int]) -> [[int]]:
        """
        very slow
        """
        res = set()
        n = len(nums)
        nums.sort()
        for i in range(n - 1):
            for j in range(i + 1, n):
                x, y = nums[i], nums[j]
                z = -(x + y)
                if z in set(nums[j + 1:]):
                    t = (x, y, z)
                    res.add(t)
        return list(map(list, res))
