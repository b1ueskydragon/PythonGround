class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        build = [float('inf')] * (amount + 1)  # build[x] is the minimum count to build amount x.
        build[0] = 0  # sentinel && base case.

        # we should try to deduct all of the coins
        # to find which is the last denomination that made prev count is valid and smallest
        for coin in coins:
            for x in range(coin, amount + 1):
                # we don't care what the added denomination(coin) is.
                # it was guaranteed from the prev_count. so just count 1.
                build[x] = min(build[x - coin] + 1, build[x])
        return (-1, build[amount])[build[amount] != float('inf')]
