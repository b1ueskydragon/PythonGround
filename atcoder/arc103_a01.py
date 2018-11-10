# noinspection PyDefaultArgument
def solve(size=int(input()), ary=list(map(int, input().split())), max_range=100001):
    # counter cache
    even = [0 for _ in range(max_range)]
    odd = [0 for _ in range(max_range)]

    # caching (max, index=num)
    (em, ei), (om, oi) = (0, 0), (0, 0)

    for i in range(size):
        if i % 2 == 0:
            even[ary[i]] += 1  # counting
            if even[ary[i]] > em:
                em, ei = even[ary[i]], ary[i]
        else:
            odd[ary[i]] += 1
            if odd[ary[i]] > om:
                om, oi = odd[ary[i]], ary[i]

    # replace := size - fixed
    if ei == oi:
        # most appearance in even and odd are same, use secondary maximum.
        even[ei], odd[oi] = 0, 0
        return size - max(max(even) + om, max(odd) + em)
    else:
        # use first maximum
        return size - (em + om)


print(solve())
