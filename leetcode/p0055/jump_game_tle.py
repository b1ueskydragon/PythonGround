"""
Initially positioned at the first index.
"""


class Solution:
    # DP; using reachable table.
    # O(N * M) time at worst, O(N) space; M is the maximum number from nums.
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
    # DP; optimize the using space, but still O(N) space for using visited set.
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


class Solution02:
    def canJump(self, nums: [int]) -> bool:
        # backtrack to retrieve all of the path that possible to reach.
        def reachable(pos, xs) -> bool:
            last = len(xs) - 1
            if pos == last:
                return True
            max_reachable = min(pos + xs[pos], last)
            pos_end = max_reachable
            while pos_end > pos:  # a bit optimization; retrieve from right to left.
                if reachable(pos_end, xs):
                    return True
                pos_end -= 1
            return False

        return reachable(0, nums)
