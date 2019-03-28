"""
base case      [] -> [] (itself)
standard case [1] -> [1], [] ([] is a previous subset)
"""


class Solution:
    cache, res = [], []

    def subsetsWithDup(self, nums):
        if not nums:  # base case. add itself.
            self.cache.append(nums)
            self.res.append(nums)
            return []

        else:  # standard case. divide
            self.subsetsWithDup(nums[1:])

            for l in self.cache:
                curr = l + nums[:1]
                if curr not in self.res:
                    self.res.append(curr)

            self.cache.append(nums[:1])

        return self.res if nums in self.res else self.res + [nums]


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 3]))
