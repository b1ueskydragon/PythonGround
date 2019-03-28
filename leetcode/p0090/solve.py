"""
base case      [] -> [] (itself)
standard case [1] -> [1], [] ([] is a previous subset)
"""


class Solution:
    cache = []

    def subsetsWithDup(self, nums):
        if not nums:  # base case. add itself.
            self.cache.append(nums)

        else:  # standard case. divide
            self.subsetsWithDup(nums[1:])

            for l in self.cache:
                print(l + nums[:1])

            self.cache.append(nums[:1])

        return self.cache


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 3]))
