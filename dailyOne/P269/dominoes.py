"""
Not correct.
"""


def solve(bs):
    """
    O(n) time,
    more than O(n) memories (?)
    """
    blocks = list(bs)
    changed = 0

    # ->
    for i, b in enumerate(blocks, 1):
        if b == "R" and blocks[i] == ".":
            blocks[i] = "R"
            changed += 1
        else:
            continue

    change = changed // 2

    # <-
    # given `blocks` in for-loop, might be not modified while looping
    for i, b in reversed(list(enumerate(blocks, start=-1))):
        if b == "L":
            if blocks[i] == ".":
                blocks[i] = "L"
            else:
                if change > 0:
                    blocks[i] = "L"
                    change -= 1
                else:
                    continue

    print(''.join(blocks))


given = ".L.R....L"  # LL.RRRLLL
# given = "..R...L.L"  # ..RR.LLLL
solve(given)
