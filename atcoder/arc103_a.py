# https://beta.atcoder.jp/contests/arc103/tasks/arc103_a

"""
- 数列に現れる数はちょうど2種類
- 偶数長の数列
- [a,b,a,b,a,b,...,b] にするための書き換える要素の最小の数
"""


# TODO refactor
def solve(ary):
    # edge case - only one or zero element
    if len(set(ary)) < 2:
        return len(ary) // 2

    # mapping each number and frequencies
    freq = {}
    nums = list(set(ary))
    for _ in nums:
        freq[_] = ary.count(_)

    # split to [e,e,e,e...,e] [o,o,o,o,...o]
    even, odd = [], []
    for i, _ in enumerate(ary):
        if i % 2 == 0:
            even.append(_)
        else:
            odd.append(_)

    # Nothing to fix
    if odd[0] != even[0] and len(set(odd)) == len(set(even)):
        return 0

    curr_max = 0
    most_freq_key = 0

    for n, f in freq.items():
        if curr_max < f:
            curr_max = f
            most_freq_key = n

    freq.pop(most_freq_key)

    curr_max = 0
    sec_freq_key = 0

    for n, f in freq.items():
        if curr_max < f:
            curr_max = f
            sec_freq_key = n

    e_size, o_size = len(even), len(odd)

    return min(e_size - even.count(most_freq_key)
               + o_size - odd.count(sec_freq_key),
               e_size - even.count(sec_freq_key)
               + o_size - odd.count(most_freq_key))


datum00 = [3, 1,
           3, 2]  # 1

datum01 = [105, 119,
           105, 119,
           105, 119]  # 0

datum02 = [1, 1,
           1, 1]  # 2

datum03 = [1, 1,
           2, 1,
           1, 3,
           1, 2,
           1, 1,
           1, 2,
           1, 1,
           1, 2,
           1, 1,
           1, 2]  # 7

print(solve(datum00))
print(solve(datum01))
print(solve(datum02))
print(solve(datum03))
