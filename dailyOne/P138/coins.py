cents = [25, 10, 5, 1]


def count_min(n):
    """
    :param n: n cents
    :return: min number of coins required
    """
    cnt = 0
    for cent in cents:
        if cent > n:
            continue
        tmp_cnt = n // cent
        n -= tmp_cnt * cent
        cnt += tmp_cnt
    return cnt


print(count_min(n=int(input())))
