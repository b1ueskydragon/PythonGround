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
