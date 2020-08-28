class Solution:
    def divisorGame(self, N: int) -> bool:
        # Alice should get 2 earlier than Bob.
        return N % 2 == 0
