class Solution:
    def singleNumber(self, nums):
        """
        use extra memory to set.
        O(N) time and space.

        (1+2+4+1+2) - 2((1+2+4+1+2) - (1+2+4)) = 4

        sum(nums) - 2 * (sum(nums) - sum(set(nums)))
        = 2 * sum(set(nums)) - sum(nums)
        """
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 1]))  # 1
    print(s.singleNumber([1, 2, 4, 1, 2]))  # 4
