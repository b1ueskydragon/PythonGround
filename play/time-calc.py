def time_calc(s, t):
    """
    range of min - s.
    :param s: second
    :param t: minute
    :return: (min - s) by sec
    """
    m = t.split('.')
    ms = int(m[0]) * 60 + int(m[1])
    return ms - int(s)


s = input()  # 33sec: 33
m = input()  # 1m 19sec: 1.19
print(time_calc(s, m))
