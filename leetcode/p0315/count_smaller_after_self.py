class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        if not nums: return []
        min_n = min(nums)
        if min_n < 0:
            nums = list(map(lambda x: x + abs(min_n), nums))
        max_n = max(nums)
        frequencies = [0] * (max_n + 1)
        for num in nums:
            frequencies[num] += 1
        res = []
        for num in nums:
            res.append(sum(frequencies[:num]))
            frequencies[num] -= 1
        return res
