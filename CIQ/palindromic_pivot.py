RANGE = 1_000_000


# 回文数ですか?
def isPal(target):
    return int(target) == int(str(target)[::-1])

# 探索だけする
def find(c1, c2):
    while (c1 <= c2):
        if isPal(c1):
            print(c1)
        c1 += 1

#真ん中だけ求める
def center(a, b):
    return int((a + b) / 2)


'''
move
pivot
'''
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
s = 28228056190
f = 77331569708
c = center(s, f)

print("真ん中", c)

calc_left(s, c)
calc_right(c, f)



# 28228056190, 77331569708 (expected 52779797725,52779897725)
# 174517247652,237309752247 (expected 205912219502,205913319502)
