def f1():
    for i in range(5):
        yield i


def f2():
    for i in range(5, 10):
        yield i


def f(f1, f2):
    for i in f1:
        yield i
    for i in f2:
        yield i


print(f(f1, f2))
