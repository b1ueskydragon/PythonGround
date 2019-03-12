class Solution:
    """
    Dynamic programming (memoize)

    we want to get an length .. not a substring itself
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        prev, curr = 0, 0
        lookup = set()

        if not s:  # exit case
            return curr
        else:  # recursive case
            for c in s:
                lookup.add(c)
                curr = len(lookup)
                if prev == curr:  # stop traversal (c is existed in lookup)
                    break
                prev = curr

            return max(curr, self.lengthOfLongestSubstring(s[1:]))


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(s="abcabcbb"))  # 3 ("abc")
    print(s.lengthOfLongestSubstring(s="bbbbb"))  # 1 ("b")
    print(s.lengthOfLongestSubstring(s="pwwkew"))  # 3 ("wke")
