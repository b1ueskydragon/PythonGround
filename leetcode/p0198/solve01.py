class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N < 3:
            return max(nums)
        p1 = nums[0]
        # chance to includes previous num.
        # if curr = a3, p2 is the max result until a2.
        p2 = nums[1]
        i = 2  # current pos init
        while i < N:
            cache = max(p1 + nums[i], p2)
            p1 = p2  # next p1
            p2 = cache  # next p2 (since has a chance to include curr)
            i += 1
        return p2
