def standardize(path):
    stack = []
    path = path.split('/')

    for seg in path:
        if seg == "..":
            if len(stack) > 1:
                stack.pop()
        elif seg == ".":
            continue
        else:
            stack.append(seg)
    return '/'.join(stack)


print(standardize(path="/usr/bin/../bin/./scripts/../"))  # /usr/bin/
print(standardize(path="/usr/bin/../bin/bin/./scripts/../scripts/"))  # /usr/bin/bin/scripts/
print(standardize(path="/usr/../"))  # /
print(standardize(path="/usr/../../"))  # /
