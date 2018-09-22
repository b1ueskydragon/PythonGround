def standardize(path):
    dirs = path.split('/')
    stair, pairs = 0, {}

    for dir in dirs:
        if dir == '..':
            stair -= 1
        elif dir != '.':
            stair += 1
            pairs[stair] = dir

    res = ''
    for s in pairs:
        if s < stair:
            res += pairs[s] + '/'
    return res


print(standardize(path="/usr/bin/../bin/./scripts/../"))  # /usr/bin/
print(standardize(path="/usr/bin/../bin/bin/./scripts/../scripts/"))  # /usr/bin/bin/scripts/
print(standardize(path="/usr/../"))  # /
print(standardize(path="/usr/../../../../bin/"))
