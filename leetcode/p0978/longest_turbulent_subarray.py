class Solution:
    def maxTurbulenceSize(self, A: [int]) -> int:
        change = [0] * len(A)  # -1 is down 1 is up 0 is equal. (↘︎ ↗ →)
        prev = A[0]
        for i, a in enumerate(A):
            if a > prev:
                change[i] = 1
            elif a < prev:
                change[i] = -1
            prev = a

        prev = -2
        max_len = 1
        incl_curr = 0
        for x in change:
            if prev != x != 0:
                incl_curr += 1
            elif x == 0:
                incl_curr = 1  # reset
            else:
                incl_curr = 2  # reset
            max_len = max(max_len, incl_curr)
            prev = x
        return max_len
