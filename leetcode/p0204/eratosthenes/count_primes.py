class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        # less than n. n instead of n + 1
        isPrime = [1] * n  # True == 1, False == 0
        isPrime[0] = 0
        isPrime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):  # consider factors
            if i != 2 and not isPrime[i]:
                continue
            for j in range(i * i, n, i):  # i < sqrt(n) is expensive than i * i < n
                isPrime[j] = 0  # loop with i step, same as j % i == 0 but faster.
        return sum(isPrime)
