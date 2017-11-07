M = 100_000


# 回文数ですか?
def isPal(target):
    return int(target) == int(str(target)[::-1])


def find(c1, c2):
    while (c1 <= c2):
        if not isPal(c1):
            c1 += 1
        else:
            return c1


def center(a, b):
    if b - a <= 374631:
        center(a, b)
    return int((a + b) / 2)


def recursion(l, r):
    c = center(l, r)

    find(l, c)
    find(c, r)



s = 28228056190
f = 77331569708

c = center(s, f)
cl = center(s, c)
cr = center(c, f)

cll = center(cl, c)
crr = center(c, cr)

clll = center(cll, c)
crrr = center(c, crr)

cllll = center(clll, c)
crrrr = center(c, crrr)

clllll = center(cllll, c)
crrrrr = center(c, crrrr)

cllllll = center(clllll, c)
crrrrrr = center(c, crrrrr)

clllllll = center(cllllll, c)
crrrrrrr = center(c, crrrrrr)

cllllllll = center(clllllll, c)
crrrrrrrr = center(c, crrrrrrr)

clllllllll = center(cllllllll, c)
crrrrrrrrr = center(c, crrrrrrrr)

cllllllllll = center(clllllllll, c)
crrrrrrrrrr = center(c, crrrrrrrrr)

clllllllllll = center(cllllllllll, c)
crrrrrrrrrrr = center(c, crrrrrrrrrr)

cllllllllllll = center(clllllllllll, c)
crrrrrrrrrrrr = center(c, crrrrrrrrrrr)

clllllllllllll = center(cllllllllllll, c)
crrrrrrrrrrrrr = center(c, crrrrrrrrrrrr)

cllllllllllllll = center(clllllllllllll, c)
crrrrrrrrrrrrrr = center(c, crrrrrrrrrrrrr)

clllllllllllllll = center(cllllllllllllll, c)
crrrrrrrrrrrrrrr = center(c, crrrrrrrrrrrrrr)

cllllllllllllllll = center(clllllllllllllll, c)
crrrrrrrrrrrrrrrr = center(c, crrrrrrrrrrrrrrr)

clllllllllllllllll = center(cllllllllllllllll, c)
crrrrrrrrrrrrrrrrr = center(c, crrrrrrrrrrrrrrrr)

cllllllllllllllllll = center(clllllllllllllllll, c) # ここ
crrrrrrrrrrrrrrrrrr = center(c, crrrrrrrrrrrrrrrrr) # ここ

print("正解r", cllllllllllllllllll)
print(c)
print("正解l", crrrrrrrrrrrrrrrrrr)


clllllllllllllllllll = center(cllllllllllllllllll, c)
crrrrrrrrrrrrrrrrrrr = center(c, crrrrrrrrrrrrrrrrrr)


print(find(cllllllllllllllllll, c))
print(find(c, crrrrrrrrrrrrrrrrrr))

print("超えたr", clllllllllllllllllll)
print(c)
print("超えたl", crrrrrrrrrrrrrrrrrrr)

print(crrrrrrrrrrrrrrrrr - clllllllllllllllll)