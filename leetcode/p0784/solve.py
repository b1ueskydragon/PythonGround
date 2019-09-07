class Solution:

    def letterCasePermutation(self, S):
        return self._dfs(S, 0, [])

    def _dfs(self, ts, i, res):
        for i in range(len(ts)):
            curr: str = ts[i]
            # TODO is alpha, is lower or upper
            self._dfs(ts, i + 1, res)
        return res
