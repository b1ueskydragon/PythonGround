class Solution:
    def __init__(self):
        self.table = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}

    def romanToInt(self, s: str) -> int:
        res = prev_num = 0
        for c in s:
            num = self.table[c]
            if prev_num < num:
                res = res - (prev_num * 2)
            res += num
            prev_num = num
        return res
