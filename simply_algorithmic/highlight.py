def input_sys():
    first_line_list = input().split(' ')
    break_point = int(first_line_list[1])

    return [first_line_list] + [(input().split(' ')) for ln in range(break_point)]


def highlight(target=input_sys()):
    # n回目ブロック数
    tail = target[1:]
    table = set()
    prev_s, prev_e = int(tail[0][0]), int(tail[0][1])
    for n, lst in enumerate(tail):
        curr_s, curr_e = int(tail[n][0]), int(tail[n][1])
        contain_s, contain_e = curr_s in table, curr_e in table

        if contain_s and contain_e and \
                curr_e < prev_e and prev_s < curr_s \
                or curr_e < prev_e and prev_s == curr_s \
                or curr_e == prev_e and prev_s < curr_s:
            [table.remove(i) for i in range(curr_s, curr_e + 1)]
        else:
            [table.add(i) for i in range(curr_s, curr_e + 1)]

        if len(table) > 0:
            prev_s, prev_e = min(table), max(table)

    return len(table)


print(highlight())
