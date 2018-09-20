def standardize(path):
    dirs = path.split('/')[1:-1]
    parent, current = "..", "."

    cursor = 0  # current position == cursor
    pair = []

    for dir in dirs:
        if dir == parent:
            cursor -= 1
        elif dir != current:
            cursor += 1
            pair.append((cursor, dir))

    return pair, cursor

    # res = ''
    # for n, d in pair:
    #     if n != cursor:
    #         res += '/' + d
    #     else:
    #         return res


given = "/usr/bin/../bin/bin/./scripts/../"  # /usr/bin/bin
print(standardize(path=given))
