class Solution:
    def letterCasePermutation(self, S):
        res = []
        self._search(S, 0, S, res)
        return res

    def _search(self, S, depth, node, res):
        res.append(node)
        for i in range(depth, len(S)):
            curr = S[i]
            # go deeper from current position
            if curr.isalpha():
                new_node = S[i].upper() if curr.islower() else curr.lower()
                self._search(S, i + 1, node[:i] + new_node + node[i + 1:], res)
            else:
                continue
