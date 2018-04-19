def power_set(lstset):
    """
    [ [], [], ... [] ] の形で出力する.

    :param lstset: set 想定の list
    :return: list の list
    """
    if not lstset:  # base case: is empty
        return [[]]
    else:
        tail = power_set(lstset[1:])
        tmp = []
        for el in tail:
            head = [lstset[0]]
            tmp += [head + el]
        return tail + tmp


print(power_set(['a', 'b', 'c']))
