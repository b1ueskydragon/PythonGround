class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ones = 0
        while xor:
            if (xor | 1) == xor:
                ones += 1
            xor >>= 1

        return ones


if __name__ == '__main__':
    s = Solution()
    """
    011
    101
    ---
    110
    count = 2
    """
    print(s.hammingDistance(3, 5))
