class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        if n < 1:
            return 0

        l, r = 0, 0  # need to add. l is "(" r is ")"
        prev = ""

        closed = s[0] == "(" and s[-1] == ")"

        # not valid pattern ((, ))
        # () is a valid pattern
        # )( is ..?
        for i, c in enumerate(s, start=1):
            if i < n and c == "(" and s[i] == "(":
                r += 1
            elif prev == ")" and c == ")":
                l += 1
            prev = c

        return (r + l + 1, r + l)[closed]


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid(s="())"))  # 1
    print(s.minAddToMakeValid(s="((("))  # 3
    print(s.minAddToMakeValid(s="))))))))))))))("))  # 15
    print(s.minAddToMakeValid(s="(((((((((((((()"))  # 13
    print(s.minAddToMakeValid(s="()))(("))  # 4
    print(s.minAddToMakeValid(s="("))  # 1
    print(s.minAddToMakeValid(s=")"))  # 1
    print(s.minAddToMakeValid(s="()()()()"))  # 0
