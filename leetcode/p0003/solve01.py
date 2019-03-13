"""
O(N) time (if worst, each char will be visited twice)
O(k) space (k is a size of the set)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr, l, r = 0, 0, 0  # curr or (r - l) should be a range
        lookup = set()
        while l < len(s) and r < len(s):
            if s[r] not in lookup:  # expand an end position
                lookup.add(s[r])
                r += 1
                curr = max(curr, r - l)
            else:  # move a start position
                lookup.remove(s[l])
                l += 1

        return curr


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(s="abcabcbb"))  # 3 ("abc")
    print(s.lengthOfLongestSubstring(s="bbbbb"))  # 1 ("b")
    print(s.lengthOfLongestSubstring(s="pwwkew"))  # 3 ("wke")
