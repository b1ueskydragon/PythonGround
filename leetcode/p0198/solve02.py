class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N < 3:
            return max(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        i = 2
        while i < N:
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            i += 1
        return dp[N - 1]
