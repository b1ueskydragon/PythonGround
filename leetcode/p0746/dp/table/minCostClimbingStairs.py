from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        total = [float('inf')] * (n + 1)  # total[i] := min-total so far to reach i. index n is the top.
        total[0], total[1] = 0, 0  # cost is non-negative
        for i in range(2, n + 1):
            total[i] = min(total[i - 2] + cost[i - 2], total[i - 1] + cost[i - 1])
        return total[-1]
