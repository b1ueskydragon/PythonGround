class Solution:
    def letterCasePermutation(self, S):
        res = []
        self._dfs(S, 0, '', res)
        return res

    def _dfs(self, S, depth, node, res):
        if depth == len(S):
            res.append(node)
            return

        curr = S[depth]
        if curr.isalpha():
            self._dfs(S, depth + 1, node + curr.upper(), res)
            self._dfs(S, depth + 1, node + curr.lower(), res)
        else:  # skip convert, just go deeper
            self._dfs(S, depth + 1, node + curr, res)
