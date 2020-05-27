class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        incl = exc_or_incl = -2147483648
        for num in nums:
            incl = max(num, num + incl)
            exc_or_incl = max(incl, exc_or_incl)
        return exc_or_incl
