class Solution:
    def letterCasePermutation(self, S):
        res = []
        self._search(S, 0, S, res)
        return res

    def _search(self, S, depth, node, res):
        res.append(node)
        for i in range(depth, len(S)):
            # go deeper from current position
            self._search(S, i + 1, node[:i] + S[i].upper() + node[i + 1:], res)


if __name__ == '__main__':
    x = Solution()
    y = x.letterCasePermutation("ab")
    print(y)
