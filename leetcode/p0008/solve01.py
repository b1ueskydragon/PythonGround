class Solution:
    def myAtoi(self, str: str) -> int:
        if not str.strip():
            return 0

        head = str.strip().split()[0]
        symbol = {'-', '+'}
        digits = ""
        for i, c in enumerate(head):
            if (i == 0 and c in symbol) or c.isdigit():
                digits += c
            else:
                digits = head[:i]
                break

        if not digits or digits in symbol:
            return 0

        is_negate = False
        if digits[0] in symbol:
            if digits[0] == '-':
                is_negate = True
            digits = digits[1:]

        res = 0
        for i, digit in enumerate(reversed(digits)):
            digit = int(digit)
            if i == 0:
                res += digit
            else:
                res += 10 ** i * digit

        if is_negate:
            res = -res

        int_max, int_min = 2 ** 31 - 1, -2 ** 31
        if res > int_max:
            return int_max
        elif res < int_min:
            return int_min

        return res
