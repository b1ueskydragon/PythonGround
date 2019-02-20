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
        res.append((low, high))
    if res[-1][-1] != len(blocks) - 1:
        res.append((low, high))

    return res


def solve(blocks, res=""):
    sections = boundaries(blocks)

    for section in sections:
        l, r = section
        start, end = blocks[l], blocks[r]
        times = r - l

        # section, excludes `end` in all cases
        # case 1
        if start == "." and end == "L":
            print(1)
            res += "L" * (times + 1)

        # case 2
        elif start == "." and end == "R":
            print(2)
            res += "." * times

        # case 3
        elif start == "L" and end == "R":
            print(3)
            res += "." * (times - 1)

        # case 4
        elif start == "R" and end == "L":
            print(4)
            c1 = (times + 1) // 2
            c2 = (times + 1) % 2
            res += "R" * c1 + "." * c2 + "L" * c1

        # case 5
        elif start == "L" and end == ".":
            print(5)
            res += "L" + "." * times

        # case 6
        elif start == "R" and end == ".":
            print(6)
            res += "R" * (times + 1)

        # case 7
        elif start == "L" and end == "L":
            print(7)
            res += "L" * times

        # case 8
        elif start == "R" and end == "R":
            print(8)
            res += "R" * times

    return res


given1 = ".L.R....L"  # LL.RRRLLL
given2 = "..R...L.L"  # ..RR.LLLL
given3 = "......L"  # LLLLLLL
given4 = "L......"  # L......
given5 = "R......"  # RRRRRRR
given6 = "LRLRLR"  # ?

print(boundaries(given1))
print(solve(given1))
print(boundaries(given2))
print(solve(given2))
print(boundaries(given3))
print(solve(given3))
print(boundaries(given4))
print(solve(given4))
print(boundaries(given5))
print(solve(given5))
print(boundaries(given6))
print(solve(given6))
