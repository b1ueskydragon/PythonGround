class Solution:
    def myAtoi(self, target: str) -> int:
        if not target.strip():
            return 0

        head = target.strip().split()[0]
        symbol = {'-', '+'}
        num = ""
        for i, c in enumerate(head):
            if (i == 0 and c in symbol) or c.isdigit():
                num += c
            else:
                num = head[:i]
                break

        if not num or num in symbol:
            return 0

        num = int(num)

        # TODO digit factor (*10)
        int_max, int_min = 2 ** 31 - 1, -2 ** 31
        if num > int_max:
            return int_max
        elif num < int_min:
            return int_min

        return num
