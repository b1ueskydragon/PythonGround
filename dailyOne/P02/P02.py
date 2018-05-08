def accumulate(ary):
    acc_init = 1  # accumulation init (multiple)

    """
    running(left to right)
    """
    acc = acc_init
    fin = len(ary)
    last = fin - 1
    result = []

    for i in range(0, fin):
        result.append(acc)
        acc = acc * ary[i]

    """
    running reverse(right to left)    
    """
    acc = acc_init  # accumulation init
    for i in range(last, -1, -1):
        result[i] = result[i] * acc
        acc = acc * ary[i]

    return result


print(accumulate([1, 2, 3, 4, 5]))
print(accumulate([3, 2, 1]))
