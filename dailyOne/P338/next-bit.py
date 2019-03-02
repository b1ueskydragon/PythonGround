"""
Find the next higher number with same number of set bits.

About bit invert,
for example,

    0 - (+5) = -5

    it can be represented at binary

    10000
    - 101
     1011
     ↑
    (-)


About mask,
mask should be 1 or 10...0
and then, for example,
    ~ 100 = 1011
"""


def snoob(num):
    """
    O(N)
    N is size of integer
    """
    if not num:
        return 0

    one = 0  # the number of 1 to clear
    mask = 1

    # iterate LSB to MSB until get a 10...0
    while not ((num & mask) > 0 and (num & (mask << 1)) == 0):
        if num & mask > 0:
            one += 1
            num &= ~mask  # set the bit to 0

        mask <<= 1

    num &= ~mask  # set the bit to 0
    num |= mask << 1  # set the next highest bit to 1

    for i in range(one):
        num |= 1 << i

    print(num, bin(num)[2:])


snoob(6)  # 110 (6) -> 1001 (9)
snoob(12)  # 1100 (12) -> 10001 (17)
snoob(8)  # 1000 (8) -> 10000 (16)
snoob(31)  # 11111 (31) -> 101111
snoob(156)  # 10011100 (156) -> 10100011 (163)
