def products(ary):
    left = 1
    right = len(ary)
    result = []

    for i in range(0, right):
        result.append(left)
        left = left * ary[i]

    left = 1
    for i in range(right - 1, -1, -1):
        result[i] = result[i] * left
        left = left * ary[i]

    return result


print(products([1, 2, 3, 4, 5]))
