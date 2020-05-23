class Solution:
    # count straightforward.
    # # O(N^2) Time O(N) Space.
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        count = dict()
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        res = [0] * len(nums)
        for i, x in enumerate(nums):
            for k in count:
                if k < x:
                    res[i] += count[k]

        return res
