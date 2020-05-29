class Solution:
    def maxTurbulenceSize(self, A: [int]) -> int:
        change = [0] * len(A)  # -1 is down 1 is up 0 is equal. (↘︎ ↗ →)
        prev = A[0]
        for i, a in enumerate(A):
            if a > prev:
                change[i] = 1
            elif a < prev:
                change[i] = -1
            else:
                change[i] = 0
            prev = a

        prev = -2
        max_len = 1
        incl_curr = 0
        i = 0
        while i < len(A):
            if prev != change[i] != 0:
                incl_curr += 1
            elif change[i] == 0:
                incl_curr = 1
            else:
                incl_curr = 2
            max_len = max(max_len, incl_curr)
            prev = change[i]
            # print(i, incl_curr)
            i += 1
        return max_len
