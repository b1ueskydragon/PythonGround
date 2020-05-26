class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        N = len(nums)
        sofar = [0] * N
        sofar[0] = nums[0]  # the max current sum that includes nums[i]
        for i in range(1, N):
            sofar[i] = max(nums[i], sofar[i - 1] + nums[i])
        return max(sofar)
