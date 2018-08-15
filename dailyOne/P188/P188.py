"""
How can we make it print out what we apparently want?
"""

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        print(i)

        def print_i():
            pass

        flist.append(print_i)

    return flist


functions = make_functions()
for f in functions:
    f()
