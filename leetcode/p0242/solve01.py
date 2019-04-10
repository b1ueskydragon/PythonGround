class Solution:
    def hashtable(self, s: str):
        pair = {}  # {char : count}
        for c in s:
            if c not in pair:
                pair[c] = 1
            else:
                pair[c] += 1

        return pair

    def isAnagram(self, s: str, t: str) -> bool:
        return self.hashtable(s) == self.hashtable(t)


if __name__ == '__main__':
    s = Solution()
    # only lowercase, may contain unicode characters
    print(s.isAnagram("anagram", "mngrama"))  # false
    print(s.isAnagram("anagra?m!", "n!aga?ram"))  # true
