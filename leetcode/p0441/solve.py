class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        n = (1 + k) * k / 2
        k^2 + k - 2n = 0

        apply Quadratic formula to find k
        k =　(-1 + (1 + 8n ) ^ 1/2) / 2

        find natural number k ( ~ 2^31 -1)
        """
        return int(((1 + 8 * n) ** 0.5 - 1) * 0.5)

    def arrangeCoins_(self, n: int) -> int:
        """
        n = (1 + k) * k / 2
        2n = k + k^2

        make to Perfect squares
        2n + 1/4 = k^2 + k + 1/4
        2n + 1/4 = (k + 1/2)^2

        (2n + 1/4) ^ 1/2 = k + 1/2  (k >= 0)
        k = (2n + 1/4) ^ 1/2 - 1/2

        * Quadratic formula could be proved by Perfect squares,
          so this is identically same as above actually.
        """
        return int((n * 2 + 0.25) ** 0.5 - 0.5)
