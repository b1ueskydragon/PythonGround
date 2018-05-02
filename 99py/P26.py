def combinations(n, origin):
    rst = []
    c_helper(outer=rst, each_stk=[], stk_len=n, current=origin)

    return rst


def c_helper(outer, each_stk, stk_len, current):
    if len(each_stk) is stk_len:
        outer.append(each_stk)
        return outer

    generatable = len(current) + len(each_stk) >= stk_len

    if not generatable:
        return outer

    if generatable:
        c_helper(outer, [current[0]] + each_stk, stk_len, current[1:])
        return c_helper(outer, each_stk, stk_len, current[1:])


print(combinations(2, ['a', 'b', 'c']))
