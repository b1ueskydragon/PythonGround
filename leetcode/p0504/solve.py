class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        :param num: num is in range of [-1e7, 1e7]
        :return: the base7 converted str num
        """
        res = 0
        digit = 1
        n = abs(num)
        while n:
            res += (digit * (n % 7))
            digit *= 10
            n //= 7
        if num < 0:
            res *= -1
        return str(res)
