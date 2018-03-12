def time_calc(s, m):
    """
    range of time by sec.

    :param s: second
    :param m: minute
    :return: (min - s) by sec
    """
    s = min_to_sec(s)
    m = min_to_sec(m)
    return m - s


def min_to_sec(t):
    """
    convert min to sec.

    :param t: time
    :return: second
    """
    t = t.split('.')
    return int(t[0]) * 60 + int(t[1])


s = input()  # 33sec: 0.33
m = input()  # 1m 19sec: 1.19
print(time_calc(s, m))

# TODO Exception Handling
