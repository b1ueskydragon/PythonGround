class Solution:
    """
    judge x が存在するとき,

    [1...n], 任意の n に対して [n, x] が存在,
                            [x, n] が存在しない.
    """

    def findJudge(self, N: int, trust: [[int]]) -> int:
        citz = [0] * N  # create indices
        trustee = set()

        judge = N * (N + 1) // 2

        for (c, j) in trust:
            citz[c - 1] = c
            trustee.add(j)

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(N=1, trust=[]))
    print(s.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))
    print(s.findJudge(N=3, trust=[[1, 2], [2, 3]]))  # 1->3 not exists, return -1
    print(s.findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
