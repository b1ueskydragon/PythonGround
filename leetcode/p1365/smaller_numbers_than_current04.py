class Solution:
    # use constraints.
    # 2 <= nums.length <= 500
    # 0 <= nums[i] <= 100
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        N, LIM = len(nums), 101
        freq = [0] * 101
        for x in nums:
            freq[x] += 1
        # in-place; now freq[num] be the count which is <= num
        for num in range(1, LIM):
            freq[num] += freq[num - 1]
        return [freq[x - 1] if x > 0 else 0 for x in nums]
