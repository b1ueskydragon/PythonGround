class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if not prices:
            return 0
        res = 0
        mp = max(prices)
        last = len(prices) - 1
        for i, v in enumerate(prices):
            res = max(res, mp - v)
            if v == mp and i < last:
                mp = max(prices[i + 1:])
        return res
