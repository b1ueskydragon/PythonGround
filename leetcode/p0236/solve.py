def solve(root, p, q):
    # All of the nodes' values will be unique.
    l, r = root.index(p), root.index(q)

    i1 = (l - 1) // 2 if l > 0 else 0
    i2 = (r - 2) // 2 if r > 0 else 0

    while i1 < i2:  # i1 is upper then i2
        i2 = (i2 - 2) // 2
        if i2 == l:
            return root[l]

    while i1 > i2:  # i2 is upper then i1
        i1 = (i1 - 1) // 2
        if i1 == r:
            return root[r]

    if i1 == i2:
        return root[i1]


root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
print(solve(root, p=5, q=1))  # 3
print(solve(root, p=6, q=4))  # 5
print(solve(root, p=5, q=4))  # 5
print(solve(root, p=3, q=7))  # 3
