"""
O(N^2) time and O(1) space
"""


class Solution:
    def _valid_max(self, s: str, l: int, r: int) -> int:
        # expand edges
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        l, r = 0, 0
        for i, _ in enumerate(s):
            curr = max(self._valid_max(s, i, i), self._valid_max(s, i, i + 1))

            if curr > r - l:
                l = i - (curr - 1) // 2
                r = i + curr // 2

        return s[l: r + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome(s="babad"))  # bab or aba
    print(s.longestPalindrome(s="cbbd"))  # bb
    print(s.longestPalindrome(s="babadadadb"))  # dadad
