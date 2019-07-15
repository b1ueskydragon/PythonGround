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
