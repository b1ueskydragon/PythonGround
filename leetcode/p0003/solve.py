class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev, curr = 0, 0
        # TODO Dynamic programming (memoize)
        # we want to get an length .. not a substring itself
        return max(prev, curr)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(s="abcabcbb"))  # 3 ("abc")
    print(s.lengthOfLongestSubstring(s="bbbbb"))  # 1 ("b")
    print(s.lengthOfLongestSubstring(s="pwwkew"))  # 3 ("wke")
