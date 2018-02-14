""""
closures
returns a new anonymous function
"""


# constructs a pair
def cons(a, b):
    return lambda f: f(a, b)


# returns the first element
def car(pair):
    return pair(lambda a, b: a)


# returns the last element
def cdr(pair):
    return pair(lambda a, b: b)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
print(cdr(cdr(cons(3, cons(3, 4)))))
