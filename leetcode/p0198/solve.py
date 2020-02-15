class Solution:
    # each num is bigger than 0
    def rob(self, nums: [int]) -> int:
        inc = 0  # includes curr
        exc = 0  # excludes curr
        prev_inc = 0  # includes adjacent prev of curr
        prev_exc = 0  # excludes adjacent prev of curr
        res = 0
        curr = 0
        # O(N)
        while curr < len(nums):
            inc = nums[curr] + prev_exc
            exc = prev_inc
            res = max(inc, exc)
            prev_exc = max(prev_inc, prev_exc)
            prev_inc = inc
            curr += 1
        return res
