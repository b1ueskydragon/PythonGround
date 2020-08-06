class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return int(num ** 0.5) ** 2 == num
        limit = 2 ** 31 - 1
        for i in range(1, 2 ** 16):
            ii = i * i
            if ii > limit:
                return False
            if num == ii:
                return True
        return False
