"""
Tip
  - Find a specific pattern (base/standard)
    from example cases at first.
"""


def gray_code(bit: int):
    """
    O(2^n)
    """

    # empty handling
    if not bit:
        return []

    """base case"""
    if bit == 1:
        return [0, 1]

    """
    standard case
      - duplicate prev status at first and add a 0 to prefix.
      - mirror-reversing and add a 1 to prefix.
    """

    prev = gray_code(bit - 1)
    prev_f = [f'0{k}' for k in prev]
    curr = prev_f + [f'1{k}' for k in list(reversed(prev))]

    return curr


print(gray_code(1))
print(gray_code(2))
print(gray_code(3))
print(gray_code(4))

# TODO Try with shift op
