def pick3th(xs):
    res = []
    pos = 2
    while pos < len(xs):
        res.append(xs.pop(pos))
        pos += 2
        if pos >= len(xs):
            pos -= len(xs)  # revert
    while xs:
        res.append(xs.pop(0))

    return res


def pick3th_another(xs):
    res = []
    i = 0
    while len(xs) > 0:
        i = (i + 2) % len(xs)  # revert
        res.append(xs.pop(i))
    return res
