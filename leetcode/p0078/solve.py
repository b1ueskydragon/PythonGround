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

    def subsets__(self, nums):
        """
        res                     : nums
        [       []      ]       : []
        [   [],      [1]]       : [1]
        [[], [2], [1], [1,2]]   : [1,2]
        ...                       ...
        """
        res = []
        if nums:
            for sub in self.subsets__(nums[:-1]):
                res.append(sub)
                new_sub = sub.copy()
                new_sub.append(nums[-1])
                res.append(new_sub)
        else:
            res.append([])
        return res

    def subsets___(self, nums):
        res = []
        if nums:
            for sub in self.subsets___(nums[:-1]):
                new_sub = sub.copy()
                new_sub.append(nums[-1])
                res.append(new_sub)
                res.append(sub)
        else:
            res.append([])
        return res
