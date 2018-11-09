# https://beta.atcoder.jp/contests/arc103/tasks/arc103_a


def given(_dummy=int(input())): return [int(_) for _ in input().split()]


def solve(ary):
    if len(set(ary)) < 2:
        return len(ary) // 2

    even, odd = [], []
    for i, _ in enumerate(ary):
        even.append(_) if i % 2 == 0 else odd.append(_)

    even_key, odd_key = list(set(even)), list(set(odd))

    res = len(ary)
    most = 0

    if len(even_key) != 1:
        l_cache = 0
        for n in even:
            curr = max(l_cache, even.count(n))
            if l_cache != curr:
                most = n
            l_cache = curr

        res -= l_cache
    else:
        res -= len(even)

    if len(odd_key) != 1:
        r_cache = 0
        for n in odd:
            if n == most:
                continue
            curr = max(r_cache, odd.count(n))
            r_cache = curr

        res -= r_cache
    else:
        res -= len(odd)

    return res


print(solve(given()))
