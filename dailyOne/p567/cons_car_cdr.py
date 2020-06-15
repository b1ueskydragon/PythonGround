def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# functional composition
def car(pair):
    g = lambda a, _: a
    return pair(g)


def cdr(pair):
    g = lambda _, b: b
    return pair(g)
