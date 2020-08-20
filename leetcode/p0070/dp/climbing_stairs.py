class Solution:
    """
    [2] := [1] + 1, [0] + 2
    [3] := [2] + 1, [1] + 2
    [4] := [3] + 1, [2] + 2
    ...
    """
    def climbStairs(self, n: int) -> int:
        count = [0] * (n + 1)
        count[0] = 1
        count[1] = 1
        for stair in range(2, n + 1):
            count[stair] = count[stair - 1] + count[stair - 2]
        return count[-1]
