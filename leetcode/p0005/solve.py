class Solution:
    # len(s) <= 1000
    # TODO deque
    def longestPalindrome(self, s: str) -> str:
        curr = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                ll, rr = l, r
                while ll < rr:
                    if s[ll] == s[rr]:
                        ll += 1
                        rr -= 1
                    else:
                        break
                else:
                    curr = max(curr, r - l + 1)

                l += 1
                r = len(s) - 1
            else:
                r -= 1

        return max(curr, r - l + 1)


if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome(s="babad"))  # bab or aba
    print(s.longestPalindrome(s="cbbd"))  # bb
