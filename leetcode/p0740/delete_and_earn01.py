class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        limit = 10001  # nums[i] is an integer in the range [1, 10000]
        order = [0] * limit
        for num in nums:
            order[num] += num
        # delete == cannot select anymore; can convert a non-adjacent max sum problem
        res = [0] * limit
        res[0] = order[0]
        for i in range(1, limit):  # [i] + [i-2] so far VS [i-1] so far
            res[i] = max(res[i - 2] + order[i], res[i - 1])
        return max(res)
