outer = []


def combinations(n, origin):
    c_helper([], n, origin)
    return outer


def c_helper(each_stk, stk_len, current):
    if len(each_stk) is stk_len:
        outer.append(each_stk)
        return outer

    generatable = len(current) + len(each_stk) >= stk_len
    if generatable:
        c_helper([current[0]] + each_stk, stk_len, current[1:])
        c_helper(each_stk, stk_len, current[1:])


print(combinations(2, ['a', 'b', 'c']))
