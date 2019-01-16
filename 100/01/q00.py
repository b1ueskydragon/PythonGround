def solve(msg):
    xs = list(msg)

    last = len(xs) - 1
    for i in range(len(xs) // 2):
        xs[i], xs[last - i] = xs[last - i], xs[i]

    print(''.join(xs))


def solve_(msg):
    print(''.join(reversed(list(msg))))


given = "stressed"
solve(given)
solve_(given)
