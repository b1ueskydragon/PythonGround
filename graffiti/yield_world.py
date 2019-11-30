def f1():
    for i in range(5):
        yield i


def f2():
    for i in range(5, 10):
        yield i


def f(_f1, _f2):
    for i in _f1():
        yield i
    for i in _f2():
        yield i


def f_(_f1, _f2):
    yield from _f1()
    yield from _f2()


print(list(f(f1, f2)))
print(list(f_(f1, f2)))
