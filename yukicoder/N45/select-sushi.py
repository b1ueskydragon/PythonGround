def non_adjacent_max_sum(putlen=input(), putnum=input()):
    lookup_lane = []
    for sn in putnum.split(' '):
        sn = int(sn)
        lookup_lane.append(sn)
    """
    [[ init approach ]]
    手動で比較する時どういう方法で比較するのか.

    その都度の sum を記録しながら操作(覚える)
    必要によっては前回の選択肢を捨てる(置き換える)
    -> 一つ前の段階を逆算して考える.
    """
    previous_sum_non_adjacent = 0
    previous_sum_adjacent = 0

    for idx, lookup in enumerate(lookup_lane):
        lookup_included_sum = lookup + previous_sum_non_adjacent  # 一つ前までの sum (最後の点が隣接しない) と着目点を足し合わす
        lookup_excluded_sum = max(previous_sum_adjacent, previous_sum_non_adjacent)

        previous_sum_non_adjacent = lookup_excluded_sum
        previous_sum_adjacent = lookup_included_sum

    return max(lookup_excluded_sum, lookup_included_sum)


print(non_adjacent_max_sum())
