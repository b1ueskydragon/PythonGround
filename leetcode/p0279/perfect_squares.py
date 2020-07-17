class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for k in range(1, n + 1):
            i = 1
            while i * i <= k:
                dp[k] = min(dp[k], dp[k - i * i] + 1)
                i += 1
        return dp[-1]
