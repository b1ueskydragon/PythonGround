class Solution:
    def maxProduct(self, nums: [int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        if N == 1:
            # if there is only one number, that's the result.
            return nums[0]
        """
        There are two signs, so two caches required.        
        cache[i] := max or min result until i'th.
        each cache result can be used and move to different cache.
        """
        max_cache = [0] * N
        min_cache = [0] * N
        max_cache[0] = min_cache[0] = nums[0]
        for i in range(1, N):
            curr, prev_max_res, prev_min_res = nums[i], max_cache[i - 1], min_cache[i - 1]
            max_cache[i] = max(curr, curr * prev_max_res, curr * prev_min_res)
            min_cache[i] = min(curr, curr * prev_max_res, curr * prev_min_res)
        return max(max_cache)
