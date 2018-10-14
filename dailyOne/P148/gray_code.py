"""
Reflecting the Hamming distance of 1 between adjacent codes.

In n bit, Hamming distance could be taken 2^0 ~ 2^(n-1).
e.g) 2 bit
    - Result of XOR is 01 or 10 between adjacent codes.
"""


def gray_code(bit: int) -> list:
    """
    O(2^n) time
    """

    # Maximum digit could be taken
    max_n = 2 ** bit

    # make an XOR between k and 1bit right shifted k
    res = [f'{k ^ (k >> 1):0{bit}b}' for k in range(max_n)]

    return res


print(gray_code(bit=2))
print(gray_code(bit=3))
print(gray_code(bit=4))

# TODO Try memoization
