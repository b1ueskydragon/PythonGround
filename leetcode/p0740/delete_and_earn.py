class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        limit = 10001  # nums[i] is an integer in the range [1, 10000]
        order = [0] * limit
        for num in nums:
            order[num] += num
        # delete == cannot select anymore; can convert a non-adjacent max sum problem
        incl_prev = excl_prev = res = 0
        for curr in order:
            incl_curr = curr + excl_prev
            res = max(incl_prev, incl_curr)
            excl_prev = max(incl_prev, excl_prev)  # exclude the curr only.
            incl_prev = incl_curr
        return res
