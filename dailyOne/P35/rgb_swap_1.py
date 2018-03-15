table = {}


def enroll_hash(ary):
    r_hash = hash('R')
    g_hash = hash('G')
    b_hash = hash('B')

    r_cnt = 0
    g_cnt = 0
    b_cnt = 0

    for e in ary:
        if hash(e) == r_hash:
            r_cnt += 1
            table[r_hash] = r_cnt
        if hash(e) == g_hash:
            g_cnt += 1
            table[g_hash] = g_cnt
        if hash(e) == b_hash:
            b_cnt += 1
            table[b_hash] = b_cnt

    return table


def swap_in_place(ary, _hash, _cnt):
    swap_idx = 0

    for i, v in enumerate(ary):
        if hash(v) == _hash:
            ary[i], ary[swap_idx] = ary[swap_idx], ary[i]
            swap_idx += 1

            if swap_idx == _cnt:
                break

    return ary


ary = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
enroll_hash(ary)

for k in table:
    swap_in_place(ary, k, table[k])

print(ary)
