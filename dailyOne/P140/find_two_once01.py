# { k : cnt } mapping
# { cnt : (k1, k2 ..) } mapping ?
# table = {2: set(), 1: set()}
def find_two_once_01(ary):
    table = {}
    for k in ary:
        cnt = 1
        if table.get(k) is 1:
            cnt += 1
        table.update({k: cnt})

    rst = []
    [rst.append(kc) for kc in table if table.get(kc) is 1]
    return rst


given = [2, 4, 6, 8, 10, 2, 6, 10]
print(find_two_once_01(given))
