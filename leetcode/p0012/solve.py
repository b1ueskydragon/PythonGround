class Solution:
    def __init__(self):
        self.dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"
            , 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        self.res = ""

    def _convert(self, x, digit):
        if x in self.dict:
            return self.dict[x]
        else:
            five = digit * 5
            if x < five:
                return self.dict[digit] * (x // digit)
            else:  # max is 3999
                return self.dict[five] + self.dict[digit] * ((x - five) // digit)

    def intToRoman(self, num: int) -> str:
        digit = 10 ** (len(str(num)) - 1)
        while num > 0:
            x = (num // digit) * digit
            self.res += self._convert(x, digit)
            num %= digit
            digit //= 10
        return self.res
