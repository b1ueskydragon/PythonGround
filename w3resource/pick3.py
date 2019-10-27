# input
alphas = [chr(i) for i in range(97, 123)]
nums = [10 * i for i in range(1, 10)]


def pick3th(xs, res):
    pos = 2
    while xs and pos < len(xs):
        res.append(xs.pop(pos))
        pos += 2
        if pos >= len(xs):
            pos -= len(xs)  # revert
    while xs:
        res.append(xs.pop(0))

    return res


def pick3th_another(xs, res):
    i = 0
    while len(xs) > 0:
        i = (i + 2) % len(xs)  # revert
        res.append(xs.pop(i))
    return res


print(pick3th(nums.copy(), []))
print(pick3th_another(nums.copy(), []))
print(pick3th(alphas.copy(), []))
print(pick3th_another(alphas.copy(), []))
