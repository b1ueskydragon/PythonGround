class Solution:
    def arrangeCoins(self, n: int) -> int:
        acc = k = 0  # k stairs
        while acc <= n:
            k += 1
            acc += k
        return k - 1

    def arrangeCoins_(self, n: int) -> int:
        k = 0
        while n > 0:
            k += 1
            n -= k
        return k if n == 0 else k - 1
