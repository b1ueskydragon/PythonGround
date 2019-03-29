"""
 011
^101
----
 110 < res
-  1
----
 101
&110
----
 100 < erase most right `1` once, from res
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ones = 0

        while xor:
            xor &= (xor - 1)
            ones += 1

        return ones


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(3, 5))
