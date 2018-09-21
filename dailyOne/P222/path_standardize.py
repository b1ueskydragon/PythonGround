def standardize(path):
    dirs = path.split('/')
    parent, current = "..", "."

    stair, pairs = 0, {}

    for dir in dirs:
        if dir == parent:
            stair -= 1
        elif dir != current:
            stair += 1
            pairs[stair] = dir

    res = ''
    for s in pairs:
        if s < stair:
            res += pairs[s] + '/'

    return res


print(standardize(path="/usr/bin/../bin/./scripts/../"))  # /usr/bin/
print(standardize(path="/usr/bin/../bin/bin/./scripts/../scripts/"))  # /usr/bin/bin/scripts/
