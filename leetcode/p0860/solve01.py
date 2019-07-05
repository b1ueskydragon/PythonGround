class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        fives, tens = 0, 0  # count
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                tens += 1
                if fives:
                    fives -= 1
                else:
                    return False
            else:
                if fives and tens:  # 10, 5
                    fives -= 1
                    tens -= 1
                elif fives >= 3:  # 5, 5, 5
                    fives -= 3
                else:
                    return False
        return True
