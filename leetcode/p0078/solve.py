class Solution:
    """
    Given a set of distinct integers.
    """

    def subsets(self, nums: [int]) -> [int]:
        res = []

        def _dfs(xs, pos, node):
            if pos == len(xs):
                res.append(node)
                return

            _dfs(xs, pos + 1, [xs[pos]] + node)
            _dfs(xs, pos + 1, node)

        _dfs(nums, 0, [])

        return res
