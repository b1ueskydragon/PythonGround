"""
Reflecting the Hamming distance of 1 between adjacent codes.

e.g) 2 bit
    - Result of XOR is 01 or 10 between adjacent codes.
"""


def gray_code(bit: int, res=[]) -> list:
    # Hamming distance could be taken. n bit, 2^0 ~ 2^(n-1).
    distance = {2 ** n for n in range(bit)}

    # Maximum digit could be taken
    max_n = 2 ** bit

    # before convert to gray
    ori = [_ for _ in range(max_n)]

    return res


print(gray_code(bit=2))

# excepted
print(0 ^ 1)  # 01 2^0
print(1 ^ 3)  # 10 2^1
print(3 ^ 2)  # 01 2^0
print(2 ^ 0)  # 10 2^1
