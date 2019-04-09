class Solution:
    def twoSum(self, nums, target):
        pairs = {}  # O(N) space
        for i, x in enumerate(nums):  # O(N) time
            y = target - x
            if y in pairs.keys():  # lookup previous in O(1) with hash table
                return [pairs[y], i]

            pairs[x] = i


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums=[_ for _ in range(0, 25197)], target=16021))
