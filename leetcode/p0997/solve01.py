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


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(N=1, trust=[]))  # 1
    print(s.findJudge(N=2, trust=[[1, 2]]))  # 2
    print(s.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))  # judge trusts nobody, -1
    print(s.findJudge(N=3, trust=[[1, 3], [2, 3], [2, 1]]))  # 3
    print(s.findJudge(N=3, trust=[[1, 2], [2, 3]]))  # 1->3 not exists, -1
    print(s.findJudge(N=3, trust=[[1, 2], [2, 3], [1, 3]]))  # 3
    print(s.findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 3
