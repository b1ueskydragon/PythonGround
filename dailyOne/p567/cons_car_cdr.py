def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# functional composition
def car(g):
    h = lambda a, _: a
    return g(h)


def cdr(g):
    h = lambda _, b: b
    return g(h)
