class Solution:
    def __init__(self):
        self.dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"
            , 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        self.res = ""

    def _convert(self, x):
        if x in self.dict:
            return self.dict[x]
        else:
            if 0 < x < 10:
                if x < 5:
                    return "I" * (x // 1)
                else:
                    return "V" + "I" * (abs(5 - x) // 1)
            elif 10 < x < 100:
                if x < 50:
                    return "X" * (x // 10)
                else:
                    return "L" + "X" * (abs(50 - x) // 10)
            elif 100 < x < 1000:
                if x < 500:
                    return "C" * (x // 100)
                else:
                    return "D" + "C" * (abs(500 - x) // 100)
            else:  # max is 3999
                return "M" * (x // 1000)

    def intToRoman(self, num: int) -> str:
        digit = 10 ** (len(str(num)) - 1)
        while num > 0:
            x = (num // digit) * digit
            self.res += self._convert(x)
            num %= digit
            digit //= 10
        return self.res
