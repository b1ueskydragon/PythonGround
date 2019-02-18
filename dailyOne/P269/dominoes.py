def solve(bs):
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
    # loop の中で 最初の blocks は変わらない
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
