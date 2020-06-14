class Solution:
    # I prefer to solve in O(N) time instead of O(N logN) and
    # we can solve in O(N) with two pointers since A is sorted in non-decreasing order.
    def sortedSquares(self, A: [int]) -> [int]:
        N = len(A)
        l, r, i = 0, N - 1, N - 1
        res = [0] * N
        while l <= r:
            ll, rr = A[l] ** 2, A[r] ** 2
            if ll > rr:
                res[i] = ll
                l += 1
            else:
                res[i] = rr
                r -= 1
            i -= 1
        return res
