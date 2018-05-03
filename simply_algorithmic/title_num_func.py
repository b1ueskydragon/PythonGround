i = lambda y: 1 if y < -1 else i(y - 1) + i(y - 2)
j = sum([i(x) * pow(-1, x) for x in range(5)])

print(j)


def func_i(y):
    if y < -1:
        return 1
    else:
        return func_i(y - 1) + func_i(y - 2)


def func_j():
    rst_sum = 0
    for x in range(5):
        rst_sum += func_i(x) * pow(-1, x)
    return rst_sum


print(func_j())
