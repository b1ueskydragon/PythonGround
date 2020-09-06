from typing import List


# The order of output does not matter.
# There is a  limit, h < 12, m < 60.
class Solution:
    def __init__(self):
        def _ones(n, cnt=0):
            while n > 0:
                if n & 1 == 1:
                    cnt += 1
                n >>= 1
            return cnt

        def _gen_table(limit):
            table = {}
            for i in range(0, limit):
                digit = _ones(i)
                if digit not in table:
                    table[digit] = []
                table[digit].append(i)
            return table

        self.h = _gen_table(12)
        self.m = _gen_table(60)

    def readBinaryWatch(self, num: int) -> List[str]:
        h, m = self.h, self.m
        res = []
        for i in range(num + 1):
            if i not in h or num - i not in m:
                continue
            for hour in h[i]:
                for minute in m[num - i]:
                    minute = str(minute).rjust(2, '0')
                    res.append(f'{hour}:{minute}')
        return res
