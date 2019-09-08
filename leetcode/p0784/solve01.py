class Solution:
    def letterCasePermutation(self, S):
        res = []
        self._search(S, 0, S, res)
        return res

    def _search(self, S, depth, node, res):
        res.append(node)
        for i in range(depth, len(S)):
            curr = S[i]
            if curr.isalpha():
                new_node = S[i].upper() if curr.islower() else curr.lower()
                # i + 1; go deeper from current position
                self._search(S, i + 1, node[:i] + new_node + node[i + 1:], res)
