# 回文数ですか?
def is_pal(target):
    return int(target) == int(str(target)[::-1])


# 探索だけする
def find(x, y):
    while x <= y:
        if is_pal(x):
            print(x)
        x += 1


# 真ん中だけ求める
def center(a, b):
    return int((a + b) / 2)


RANGE = 1_000_000


# move, pivot
def calc_left(m, p):
    if center(m, p) - m > RANGE:
        calc_left(center(m, p), p)
    else:
        find(m, p)


def calc_right(p, m):
    if m - center(p, m) > RANGE:
        calc_right(p, center(p, m))
    else:
        find(p, m)


'''
start
finish
center
'''
s = 174517247652
f = 237309752247
c = center(s, f)

calc_left(s, c)
calc_right(c, f)


# 28228056190, 77331569708 (expected 52779797725,52779897725)
# 174517247652,237309752247 (expected 205912219502,205913319502)
