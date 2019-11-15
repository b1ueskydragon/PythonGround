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
        res = 0  # guaranteed to be within the range from 1 to 3999
        i, j = 0, 1
        while i < len(s):
            num = self.table[s[i]]
            if j < len(s):
                num_next = self.table[s[j]]
                if num < num_next:
                    num = num_next - num
                    i += 1
                    j += 1
            res += num
            i += 1
            j += 1
        return res
