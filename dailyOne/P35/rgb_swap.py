r = hash('R')
g = hash('G')
b = hash('B')


# TODO try another method (even if it ignore original rules :) )
# table = {'R': 1, 'G': 2, 'B': 3}


def swap_in_place(ary):
    swap_idx = 0

    # linear searching `R`
    cnt = 0
    for e in ary:
        if hash(e) == r:
            cnt += 1

    for i, v in enumerate(ary):
        if hash(v) == r:
            ary[i], ary[swap_idx] = ary[swap_idx], ary[i]
            swap_idx += 1

            if swap_idx == cnt:
                break

    # linear searching `G`
    cnt = 0
    for e in ary:
        if hash(e) == r:
            cnt += 1

    for i, v in enumerate(ary):
        if hash(v) == g:
            ary[i], ary[swap_idx] = ary[swap_idx], ary[i]
            swap_idx += 1

            if swap_idx == cnt:
                break

    # linear searching `B`
    cnt = 0
    for e in ary:
        if hash(e) == r:
            cnt += 1

    for i, v in enumerate(ary):
        if hash(v) == b:
            ary[i], ary[swap_idx] = ary[swap_idx], ary[i]
            swap_idx += 1

            if swap_idx == cnt:
                break

    return ary


ary = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(swap_in_place(ary))
