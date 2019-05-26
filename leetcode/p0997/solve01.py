class Solution:
    """
    if judge x exists,

    [1...n], For any n [n, x] exists,
                       [x, n] not exists.
    """

    def findJudge(self, N: int, trust: [[int]]) -> int:
        trusted = [0] * N  # trusted[i] = sum of who trust i+1
        _sum = N * (N + 1) // 2

        for c, j in trust:
            trusted[j - 1] += c
            trusted[c - 1] = -1  # judge trusts nobody

        for i, t in enumerate(trusted, start=1):
            if t == _sum - i:
                return i

        return -1
