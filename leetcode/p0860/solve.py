class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        # TODO Numeric +=
        fives = []
        tens = []

        for b in bills:
            if b == 5:
                fives.append(b)
            elif b == 10:
                tens.append(b)
                if fives:
                    b -= fives.pop()
                else:
                    return False
            else:
                if fives and tens:
                    b -= fives.pop() + tens.pop()
                elif len(fives) >= 3:
                    while b != 5:
                        b -= fives.pop()
                else:
                    return False

        return True
