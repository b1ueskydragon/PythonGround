class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        n = (1 + k) * k / 2
        k^2 + k - 2n = 0
        k :　(-1 + (1 + 8n ) ^ 1/2) / 2

        find natural number k ( ~ 2^31 -1)
        """
        return int(((1 + 8 * n) ** 0.5 - 1) * 0.5)
