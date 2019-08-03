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

    def subsets_(self, nums):
        res = [[]]
        n = len(nums)

        def _dfs(pos, node):
            if pos == n:
                return

            curr_node = node.copy()  # new node
            curr_node.append(nums[pos])
            res.append(curr_node)

            for j in range(pos + 1, n):
                _dfs(j, curr_node)

        for i in range(n):
            _dfs(i, [])

        return res
