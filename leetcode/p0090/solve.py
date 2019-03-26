"""
base case      [] -> [] (itself)
standard case [1] -> [1], [] ([] is a previous subset)
"""


class Solution:
    cache = []  # TODO: to set

    def subsetsWithDup(self, nums):
        if not nums:  # base case. add itself.
            self.cache.append(nums)

        else:  # standard case. divide
            self.cache.append(nums)
            self.cache.append(nums[:1])
            self.subsetsWithDup(nums[1:])

        return self.cache


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2]))
