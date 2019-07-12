class Solution:
    def arrangeCoins(self, n: int) -> int:
        acc = k = 0  # k stairs
        while acc <= n:
            k += 1
            acc += k
        return k - 1
