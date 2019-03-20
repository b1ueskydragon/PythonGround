"""
append or pop an last (most lately) element
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []  # need to append
        for c in s:
            if c == "(":
                stack.append(")")
            elif stack:  # c is ")" and stack is not empty
                stack.pop()

        return len(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid(s="((())"))  # 1
    print(s.minAddToMakeValid(s="()()"))  # 0
    print(s.minAddToMakeValid(s="()((()))"))  # 0
