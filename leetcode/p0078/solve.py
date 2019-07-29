class Solution:
    def subsets(self, nums: [int]) -> [int]:
        res = {}

        def _dfs(xs, pos, node):
            n, k = len(xs), len(node)
            if pos == n:
                if k in res:
                    if node not in res[k]:
                        res[k] += [node]
                else:
                    res[k] = [node]
                return

            _dfs(xs, pos + 1, [xs[pos]] + node)
            _dfs(xs, pos + 1, node)

        _dfs(nums, 0, [])
        
        flatten = []
        for ls in res.values():
            for l in ls:
                flatten.append(l)
        return flatten
