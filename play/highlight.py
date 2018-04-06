def input_sys():
    first_line_list = input().split(' ')
    break_point = first_line_list[1]

    result = []
    for line in range(int(break_point)):
        result.append(input().split(' '))

    return [first_line_list] + result


def highlight(target=input_sys()):
    # n回目ブロック数
    tail = target[1:]
    table = set()
    prev_s = int(tail[0][0])
    prev_e = int(tail[0][1])
    for n, lst in enumerate(tail):
        curr_s = int(tail[n][0])
        curr_e = int(tail[n][1])

        contain_s = curr_s in table
        contain_e = curr_e in table

        if contain_s and contain_e and curr_e < prev_e and prev_s < curr_s \
                or curr_e < prev_e and prev_s == curr_s \
                or curr_e == prev_e and prev_s < curr_s:
            for i in range(curr_s, curr_e + 1):
                table.remove(i)
        else:
            for i in range(curr_s, curr_e + 1):
                table.add(i)

        if len(table) > 0:
            prev_s = min(table)
            prev_e = max(table)

    return len(table)


print(highlight())
