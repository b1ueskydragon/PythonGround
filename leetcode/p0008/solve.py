import re


class Solution:
    def myAtoi(self, str: str) -> int:
        if not str.strip():  # trim
            return 0

        head = str.strip().split()[0]
        found = re.match(r"^[+|-]?\d+", head)

        if not found:
            return 0

        num = int(found.group(0))  # the entire match

        int_max, int_min = 2 ** 31 - 1, -2 ** 31
        if num > int_max:
            return int_max
        elif num < int_min:
            return int_min

        return num
