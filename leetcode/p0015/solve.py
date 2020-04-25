class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = []
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for x in count:
            if count[x] > 1 and -2 * x in count:
                if x == 0 and count[x] < 3:
                    continue
                res.append((x, x, -2 * x))

        nums = list(count.keys())  # all unique
        for i, x in enumerate(nums):
            ref = set()
            for j in range(i + 1, len(nums)):
                y = nums[j]
                z = -x - y
                if z in ref:
                    res.append((x, y, z))
                else:
                    ref.add(y)
        return res
