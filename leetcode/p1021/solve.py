class Solution:
    def removeOuterParentheses(self, S):
        """
        S is a valid parentheses string
        """
        _open, _close = "(", ")"
        oc, cc = 0, 0
        part, res = "", ""

        for i, p in enumerate(S):
            if p == _open:
                oc += 1
            elif p == _close:
                cc += 1

            part += p

            if oc == cc:
                res += part[1:-1]
                part = ""

        return res
