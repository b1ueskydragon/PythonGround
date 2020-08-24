from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s1, s2 = cost[0], cost[1]
        # min-cost to reach to current stair i.
        sofar = min(s1, s2)
        # shifting a pair of candidates (start points).
        for i in range(2, len(cost)):
            s1 = s2
            s2 = sofar + cost[i]
            sofar = min(s1, s2)
        return sofar
