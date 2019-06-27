class Solution:
    def isValid(self, s: str):
        if len(s) % 2 != 0:
            return False

        pair = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if stack:
                    op = stack.pop()
                else:
                    return False

                if c != pair[op]:
                    return False

        return stack == []
