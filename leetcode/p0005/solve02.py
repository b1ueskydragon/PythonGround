class Solution:
    def _valid_max(self, s: str, l: int, r: int) -> str:
        # l and r should be middle indices
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

    def longestPalindrome(self, s: str) -> str:
        substr = ""
        for i, _ in enumerate(s):
            # base case in odd len is p(i,i); in even len is p(i,i+1)
            odd_curr = self._valid_max(s, i, i)
            even_curr = self._valid_max(s, i, i + 1)

            if len(odd_curr) > len(substr):
                substr = odd_curr

            if len(even_curr) > len(substr):
                substr = even_curr

        return substr


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome(s="babad"))  # bab or aba
    print(s.longestPalindrome(s="cbbd"))  # bb
    print(s.longestPalindrome(s="babadadadb"))  # dadad
