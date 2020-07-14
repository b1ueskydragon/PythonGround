class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            ii = i * i
            if ii >= n + 1:
                break
            dp[ii] = 1
        if dp[-1] == 1:
            return 1
        for k in range(1, n + 1):
            for i in range(1, k + 1):
                ii = i * i  # for the minimal count, at least one number should be a square num (count = 1).
                if ii >= k:
                    break
                # f(5) := f(4) + f(1)  vs f(3) + f(2)
                dp[k] = min(dp[k], dp[ii] + dp[k - (ii)])
        return dp[-1]
