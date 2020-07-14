class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for k in range(1, n + 1):
            kk = k * k
            if kk < n + 1:
                dp[kk] = 1
            for i in range(1, k + 1):
                ii = i * i
                if ii >= k: break
                dp[k] = min(dp[k], dp[ii] + dp[k - (ii)])
        return dp[-1]
