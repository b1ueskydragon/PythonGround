class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0
        for c in s:
            if c == "(":
                r += 1
            elif c == ")":
                l += 1
        return abs(r - l)


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid(s="())"))  # 1
    print(s.minAddToMakeValid(s="((("))  # 3
    print(s.minAddToMakeValid(s="))))))))))))))("))  # 15
    print(s.minAddToMakeValid(s="(((((((((((((()"))  # 13
