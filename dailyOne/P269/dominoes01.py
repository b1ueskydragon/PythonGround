"""
O(N) time and space
"""


def _boundaries(blocks):
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
    if not res or res[-1][-1] != len(blocks) - 1:
        res.append((low, high))

    print(res)  # debug
    return res


def solve(blocks):
    """
    case match
    """
    sections = _boundaries(blocks)
    blocks = list(blocks)

    for l, r in sections:
        if blocks[l] == '.' and blocks[r] == 'L':  # ← \
            blocks[l:r] = ['L'] * (r - l)

        elif blocks[l] == 'R' and blocks[r] == '.':  # / →
            blocks[l: r + 1] = ['R'] * (r - l + 1)

        elif blocks[l] == blocks[r]:  # same direction
            blocks[l:r] = blocks[l] * (r - l)

        elif blocks[l] == 'R' and blocks[r] == 'L':  # towards the center
            while l + 1 < r - 1:
                blocks[l + 1] = blocks[l]
                blocks[r - 1] = blocks[r]
                l += 1
                r -= 1

    print(''.join(blocks))


solve(".L.R....L")  # LL.RRRLLL
solve("..R...L.L")  # ..RR.LLLL
solve("......L")  # LLLLLLL
solve("L......")  # L......
solve("R......")  # RRRRRRR
solve("LRLRLR")
