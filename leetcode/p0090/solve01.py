class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        l = 0
        nums.sort()  # !
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4, 4, 4, 1, 4]))
