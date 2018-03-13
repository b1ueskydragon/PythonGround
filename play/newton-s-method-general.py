# (2)
a = [10]
b = [10]

def read(n, x):
    for k in reversed(range(-1, n)):
        read(a[k])

    for k in reversed(range(1, n)):
        b[k - 1] = k * a[k]

    for i in range(1, 101):
        f = a[n] * x + a[n - 1]
        d = b[n - 1]

        for k in reversed(range(-1, n - 2)):
            if k >= 0:
                f = f * x + a[k]
                d = d * x + b[k]

        print(x, f, d)
        x = x - f / d
