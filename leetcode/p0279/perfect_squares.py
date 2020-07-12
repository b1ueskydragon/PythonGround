class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i * i >= n + 1:
                break
            dp[i * i] = 1

        if dp[-1] == 1:
            return 1

        for k in range(1, n + 1):
            for i in range(1, (k // 2) + 1):
                # f(5) := f(4) + f(1)  vs f(3) + f(2)
                dp[k] = min(dp[k], dp[i] + dp[k - i])
        return dp[-1]
