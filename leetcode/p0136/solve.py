class Solution:
    def singleNumber(self, nums):
        """
        O(N) time and O(1) space.
        (iterate all num, and do not use extra space)

         0 ^ 1 ^ 2 ^ 1 ^ 2 = 0
         0 ^ 1 ^ 2 ^ 4 ^ 1 ^ 2 = 4
        """
        acc = 0
        for num in nums:
            acc ^= num
        return acc

    def singleNumber_(self, nums):
        """
        functional (folding)
        """
        from functools import reduce
        from operator import xor
        return reduce(xor, nums)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 1]))  # 1
    print(s.singleNumber([1, 2, 4, 1, 2]))  # 4

    print(s.singleNumber_([2, 2, 1]))  # 1
    print(s.singleNumber_([1, 2, 4, 1, 2]))  # 4
