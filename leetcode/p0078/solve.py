class Solution:
    """
    Given a set of distinct integers.
    """

    def subsets(self, nums):
        res = []

        def _dfs(pos, node):
            if pos == len(nums):
                res.append(node)
                return

            _dfs(pos + 1, [nums[pos]] + node)
            _dfs(pos + 1, node)

        _dfs(0, [])

        return res
