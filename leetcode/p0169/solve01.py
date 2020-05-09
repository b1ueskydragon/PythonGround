"""
O(N) time, O(1) space.
Boyer-Moore Voting.
"""


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        cnt, cand = 0, None
        for x in nums:
            if cnt == 0:
                cand = x  # if count is 0, reset the candidate once.
            if x == cand:
                cnt += 1
            else:
                cnt -= 1
        return cand  # only one elements can remain with non-zero count for the majority element always exists.
