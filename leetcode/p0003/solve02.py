"""
replace set to keyset

O(N) time (visit only once)
O(k) space (k is a size of the keyset)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, curr = 0, 0
        pair = {}

        for r, c in enumerate(s):
            if c in pair.keys():
                l = max(l, pair[c])  # jump l at once

            curr = max(curr, r - l + 1)
            pair[c] = r + 1

        return curr


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(s="abcabcbb"))  # 3 ("abc")
    print(s.lengthOfLongestSubstring(s="bbbbb"))  # 1 ("b")
    print(s.lengthOfLongestSubstring(s="pwwkew"))  # 3 ("wke")
