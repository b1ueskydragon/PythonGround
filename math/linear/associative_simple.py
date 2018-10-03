def for1(m, l):
    res = []
    for j in range(1, m):
        for k in range(1, l):
            res.append((j, k))

    return res


def for2(m, l):
    res = []
    for k in range(1, l):
        for j in range(1, m):
            res.append((j, k))

    return res


m, l = 5, 10
assert len(set(for1(m, l))) == len(for1(m, l))
assert len(set(for1(m, l))) == len(for2(m, l))
assert set(for1(m, l)) == set(for2(m, l))
