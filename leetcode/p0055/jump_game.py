class Solution:
    #  O(N) time and O(1) space at most.
    def canJump(self, nums: [int]) -> bool:
        last = len(nums) - 1
        pos = last
        while pos >= 0:
            # nums[pos] is the maximum accumulation of current pos,
            # determine if current position can exceed or reach as current last.
            if pos + nums[pos] >= last:
                # if exceeded or reached, update the last to the leftest position at this time.
                # we can guarantee if we reaches the pos, we can reach to the current (now the previous) last too.
                last = pos
            pos -= 1
        return last == 0
