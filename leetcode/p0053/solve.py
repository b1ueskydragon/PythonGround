class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        N = len(nums)
        sofar = [0] * N
        sofar[0] = nums[0]  # the max sum at the current index so far.
        for i in range(1, N):
            sofar[i] = max(nums[i], sofar[i - 1] + nums[i])
        return max(sofar)
