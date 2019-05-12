class Solution:
    def removeOuterParentheses(self, S):
        _open, _close = "(", ")"
        oc = 0
        res = ""

        for p in S:
            if p == _open:
                if oc != 0:  # oc == 0 and p is most outer (
                    res += p
                oc += 1
            else:
                if oc != 1:  # oc == 1 and p is most outer )
                    res += p
                oc -= 1

        return res
