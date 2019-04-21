"""
Improve speed
O(N) mem
"""

class Solution:
    def findJudge(self, N: int, trust: [[int]]) -> int:
        citizen = {c for c, j in trust}
        # At least N-1 (Everybody except a judge) ppl trust the judge.
        if N - 1 != len(citizen):
            return -1

        judge = N * (N + 1) // 2 - sum(citizen)
        _citizen = {c for c, j in trust if j == judge}

        if N - 1 != len(_citizen):
            return -1

        return judge


if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(N=1, trust=[]))  # 1
    print(s.findJudge(N=2, trust=[[1, 2]]))  # 2
    print(s.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))  # judge trusts nobody, -1
    print(s.findJudge(N=3, trust=[[1, 3], [2, 3], [2, 1]]))  # 3
    print(s.findJudge(N=3, trust=[[1, 2], [2, 3]]))  # 1->3 not exists, -1
