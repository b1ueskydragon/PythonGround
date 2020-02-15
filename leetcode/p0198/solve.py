class Solution:
    # each num is bigger than 0
    def rob(self, nums: [int]) -> int:
        inc = 0  # includes curr
        exc = 0  # excludes curr
        prev_inc = 0  # includes adjacent prev of curr
        prev_exc = 0  # excludes adjacent prev of curr
        # O(N)
        for curr in nums:
            inc = curr + prev_exc
            exc = prev_inc
            prev_exc = max(prev_inc, prev_exc)
            prev_inc = inc
        return max(inc, exc)
