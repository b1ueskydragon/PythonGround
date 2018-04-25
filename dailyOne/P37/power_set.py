def power_set(origin):
    """
    [ [], [], ... [] ] の形で出力する.

    :param origin: set 想定の list
    :return: list の list
    """
    if not origin:  # exit case: origin(==tail) is empty
        return [[]]
    else:
        tail = power_set(origin[1:])  # result
        tmp = []  # 再帰の度に初期化 (for 文のため溜めている)
        print("tail: ", tail)
        for subtail in tail:  # subtail is a list
            head = [origin[0]]  # 再帰の際に引数で渡した元origin[1:]のhead
            print("subtail: ", subtail, "  head: ", head)
            tmp += [subtail + head]
            print("tmp: ", tmp)

        current = tail + tmp
        print("current: ", current, "\n")
        return current  # kept the same result


print(power_set(['a', 'b', 'c']))


# list comprehension
def power_set_(origin):
    if not origin:
        return [[]]

    tail = power_set_(origin[1:])
    return tail + [lst + [origin[0]] for lst in tail]


print(power_set_(['a', 'b', 'c']))
