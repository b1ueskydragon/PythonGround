def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(ci):
            def print_ci():  # closure
                print(ci)

            return print_ci  # capture the current state of `i`

        flist.append(print_i(i))

    return flist


functions = make_functions()
for f in functions:
    f()
