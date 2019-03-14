"""
replace set to keyset

O(N) time (visit only once)
O(k) space (k is a size of the keyset)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr, l = 0, 0
        pair = {}  # {start char : len}

        for r, c in enumerate(s):
            if c not in pair.keys():
                curr = max(curr, r - l)
                pair[c] = curr
            else:
                l += 1

        return curr


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(s="abcabcbb"))  # 3 ("abc")
    print(s.lengthOfLongestSubstring(s="bbbbb"))  # 1 ("b")
    print(s.lengthOfLongestSubstring(s="pwwkew"))  # 3 ("wke")
