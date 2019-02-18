def boundaries(blocks):
    """
    sections
    """
    res = []
    low = high = 0

    # `high` moves entire blocks
    # `low` moves if needed
    for high, block in enumerate(blocks[1:], 1):
        if block != '.':
            res.append((low, high))
            low = high

    # edge case
    if not res:
        return  # TODO
    if res[-1][-1] != len(blocks) - 1:
        res.append((low, high))

    return res


"""
example of boundaries

. L . R . . . . L
(0, 1)
   (1, 3)
      (3,       8) 
"""
given = ".L.R....L"  # LL.RRRLLL
# given = "..R...L.L"  # ..RR.LLLL
# given = "......L"  # LLLLLLL
# given = "L......"
print(boundaries(given))
