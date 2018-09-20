def standardize(path):
    dirs = path.split('/')[:-1]
    parent, current = "..", "."

    cursor = 0  # current position == cursor
    res = []

    for dir in dirs:
        if dir == parent:
            cursor -= 1
        elif dir != current:
            res.append(dir)
            cursor += 1

    return '/'.join(res[:cursor])


given = "/usr/bin/../bin/./scripts/../"  # "/usr/bin"
print(standardize(path=given))
