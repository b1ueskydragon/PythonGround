class Solution:
    def arrangeCoins(self, n: int) -> int:
        """ Binary search """
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            acc = (1 + mid) * mid // 2
            if acc == n:
                return mid
            if acc < n:
                low = mid + 1
            else:
                high = mid - 1
        return low - 1

    def arrangeCoins_(self, n: int) -> int:
        """ Binary search (recursion) """

        def rec(low, high):
            if low > high: return low - 1
            mid = low + (high - low) // 2
            acc = (1 + mid) * mid // 2
            return mid if acc == n else rec(mid + 1, high) if acc < n else rec(low, mid - 1)

        return rec(0, n - 1)
