class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        s = list(s)
        t.sort()
        s.sort()
        return t == s


if __name__ == '__main__':
    s = Solution()
    # only lowercase, may contain unicode characters
    print(s.isAnagram("anagram", "mngrama"))  # false
    print(s.isAnagram("anagra?m!", "n!aga?ram"))  # true
