class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i, inum in enumerate(nums):
            for j, jnum in enumerate(nums):
                if i < j and inum + jnum == target:
                    return [i, j]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
