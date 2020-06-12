"""
Initially positioned at the first index.
"""


class Solution:
    def canJump(self, nums: [int]) -> bool:
        end = len(nums) - 1
        reachable = [False for _ in range(end + 1)]
        reachable[0] = True
        visited = set()
        for i in range(end):
            for acc in range(1, nums[i] + 1):
                if i + acc > end: break
                if i + acc in visited: continue
                visited.add(i + acc)
                reachable[i + acc] = True
        return False not in reachable


class Solution01:
    def canJump(self, nums: [int]) -> bool:
        end = len(nums) - 1
        reach_count = end
        visited = set()
        for i in range(end):
            for acc in range(1, nums[i] + 1):
                if i + acc > end: break
                if i + acc in visited: continue
                visited.add(i + acc)
                reach_count -= 1
        return reach_count == 0
