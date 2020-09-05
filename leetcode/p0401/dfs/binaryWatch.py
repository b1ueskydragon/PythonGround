from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        digits = [
            8, 4, 2, 1,  # combination for hour
            32, 16, 8, 4, 2, 1  # for minutes
        ]
        res = []

        # level is stair or depth of a tree
        def dfs(digits, hour, minute, i, level):
            if hour > 11 or minute > 59:
                return
            if level == 0:  # reach to the leaves
                minute = str(minute).rjust(2, '0')
                res.append(f'{hour}:{minute}')
                return

            if i < 10:
                if i < 4:
                    dfs(digits, hour + digits[i], minute, i + 1, level - 1)
                else:
                    dfs(digits, hour, minute + digits[i], i + 1, level - 1)
                # level is the lowest stack at this point
                dfs(digits, hour, minute, i + 1, level)

        dfs(digits, 0, 0, 0, num)
        return res
