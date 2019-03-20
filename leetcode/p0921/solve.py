class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0
        for c in s:
            if c == "(":  # complete balance first anyway
                r += 1
            elif r > 0:  # c is ")" and previous ")" are exist
                r -= 1
            else:  # c is ")" but there is no previous ")"
                l += 1
        return l + r


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid(s="((())"))  # 1
    print(s.minAddToMakeValid(s="()()"))  # 0
    print(s.minAddToMakeValid(s="()((()))"))  # 0
