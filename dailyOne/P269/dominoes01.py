def boundaries(blocks):
    """
    sections

    example of boundaries

    . L . R . . . . L
    (0, 1)
       (1, 3)
          (3,       8)
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


def solve(blocks, res=""):
    sections = boundaries(blocks)

    for section in sections:
        l, r = section
        start, end = blocks[l], blocks[r]

        # section, excludes `end` in all cases
        # case 1
        if start == "." and end == "L":
            res += "L" * (r - l)

        # case 2
        elif start == "." and end == "R":
            res += "." * (r - l - 1)

        # case 3
        elif start == "L" and end == "R":
            res += "." * (r - l - 1)

        # case 4
        elif start == "R" and end == "L":
            c = (r - l) // 2
            res += "R" * c + "." * (c % 2) + "L" * c

        # case 5
        elif start == "L" and end == ".":
            res += "." * (r - l - 1)

        # case 6
        elif start == "L" and end == ".":
            res += "R" * (r - l)

        # # case 7
        # elif start == "L" and end == "L":
        #     res += "L" * (r - l)
        #
        # # case 8
        # elif start == "R" and end == "R":
        #     res += "R" * (r - l)

        res += end

    return res


# given = ".L.R....L"  # LL.RRRLLL
given = "..R...L.L"  # ..RR.LLLL
# given = "......L"  # LLLLLLL
# given = "L......"
print(boundaries(given))
print(solve(given))
