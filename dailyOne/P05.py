# constructs a pair
def cons(a, b):
    return lambda f: f(a, b)

# returns the first element
def car(cons):
    return None


# returns the last element
def cdr(cons):
    return None
