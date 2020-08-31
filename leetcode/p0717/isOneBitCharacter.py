from typing import List


# The given string will always end with a zero.
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        last = len(bits) - 1
        while i < last:
            if bits[i] == 0:  # pattern 0
                i += 1
            else:  # pattern 1* (10, 11)
                i += 2
        return i == last
