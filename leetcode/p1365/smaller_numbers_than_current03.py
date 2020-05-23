class Solution:
    # use constraints.
    # 2 <= nums.length <= 500
    # 0 <= nums[i] <= 100
    # O(N) Time O(N) Space
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        N, LIM = len(nums), 101
        freq = [0] * LIM
        for x in nums:
            freq[x] += 1
        for i in reversed(range(LIM)):
            if freq[i] > 0:
                N -= freq[i]  # deduct the biggest num's frequency at this time.
                freq[i] = N
        return [freq[x] for x in nums]
