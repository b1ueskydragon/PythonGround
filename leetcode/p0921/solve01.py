"""
append or pop an last (most lately) element
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []  # need to append ")"
        buff = 0
        for c in s:
            if c == "(":
                stack.append(")")
            elif stack:  # c is ")" and stack is not empty
                stack.pop()
            else:  # c is ")" but stack is empty (need to add "(")
                buff += 1

        return len(stack) + buff


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid(s="((())"))  # 1
    print(s.minAddToMakeValid(s="()()"))  # 0
    print(s.minAddToMakeValid(s="()((()))"))  # 0
    print(s.minAddToMakeValid(s=")))"))  # 3
    print(s.minAddToMakeValid(s="(((())"))  # 2
