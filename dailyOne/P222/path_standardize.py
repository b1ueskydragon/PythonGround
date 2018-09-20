def standardize(path):
    dirs = path.split('/')[1:-1]
    parent, current = "..", "."
    cursor = 0  # current dir == cursor

    for i, dir in enumerate(dirs):
        if dir == parent:
            cursor -= 1
        elif dir == current:
            continue
        else:
            cursor += 1

    return cursor, len(dirs)


given = "/usr/bin/../bin/./scripts/../"  # "/usr/bin"
print(standardize(path=given))
