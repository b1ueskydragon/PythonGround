class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        min_points = [0] * N
        min_points[0] = prices[0]
        max_diffs = [0] * N

        for i in range(1, N):  # max_diffs[0] is always zero
            min_points[i] = min(prices[i], min_points[i - 1])
            max_diffs[i] = max(max_diffs[i - 1], prices[i] - min_points[i - 1])
        return max_diffs[-1]
