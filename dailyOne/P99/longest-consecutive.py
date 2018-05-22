"""
find the length of the longest consecutive elements sequence in O(n).
"""


def consecutive(given):
    start, end = min(given), max(given)
    to_set = set(given)

    rst = []
    for i in range(start, end + 1):
        # is_continuity を入れるタイミング
        if i in to_set:
            rst.append(i)
    return rst


given00 = [100, 4, 200, 1, 3, 2]
given01 = [40000, 50, 4000, 40001, 40003, 40004, 40005]

print(consecutive(given00))
print(consecutive(given01))


# ソート済みの ary が間隔 1 で離れているか
def is_continuity(a):
    if not a:
        return True
    last = len(a) - 1
    return last is (a[last] - a[0])
