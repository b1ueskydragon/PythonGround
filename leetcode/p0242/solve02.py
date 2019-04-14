"""
only for lowercase alpha, a to z (26 length Fixed array)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphas = [0] * 26  # a-z

        for c in s:
            alphas[ord(c) - 97] += 1

        for c in t:
            i = ord(c) - 97
            alphas[i] -= 1
            if alphas[i] < 0:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "mngrama"))  # false
