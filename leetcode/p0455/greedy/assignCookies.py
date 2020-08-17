from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookies = list(reversed(sorted(s)))
        children = list(reversed(sorted(g)))
        i, j = 0, 0
        count = 0
        while i < len(s) and j < len(g):
            if cookies[i] >= children[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count
