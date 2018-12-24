"""
Tip
  - Find a specific pattern (base/standard)
    from example cases at first.
"""


def gray_code(bit: int):
    """
    O(2^n)
    """

    # Exception handling
    if not bit:
        return []

    """base case"""
    if bit == 1:
        return [0, 1]

    """standard case"""
    cache = gray_code(bit - 1)
    # shift left 1(MSB) for make a digit, then add value
    for k in reversed(cache):
        cache.append((1 << (bit - 1)) + k)

    return cache


print(gray_code(1))
print(gray_code(2))
print(gray_code(3))
print(gray_code(4))
