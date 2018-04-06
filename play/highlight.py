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
    prev_s = int(tail[0][0])
    prev_e = int(tail[0][1])

    for n, lst in enumerate(tail):
        curr_s = int(tail[n][0])
        curr_e = int(tail[n][1])

        if prev_s < curr_s and prev_e < curr_e:
            curr_length = curr_e - prev_s + 1
            prev_e = curr_e
            prev_s = prev_s

        elif prev_s < curr_s and prev_e > curr_e:
            curr_length = curr_s - prev_s + prev_e - curr_e

        elif prev_s < curr_s and prev_e == curr_e:
            curr_length = curr_s - prev_s + 1
            prev_s = prev_s
            prev_e = curr_s

        elif prev_s > curr_s and prev_e < curr_e:
            curr_length = curr_e - curr_s + 1
            prev_e = curr_e
            prev_s = curr_s

        elif prev_s > curr_s and prev_e > curr_e:
            curr_length = prev_e - curr_s + 1
            prev_e = prev_e
            prev_s = curr_s

        elif prev_s > curr_s and prev_e == curr_e:
            curr_length = prev_e - curr_s + 1
            prev_e = prev_e
            prev_s = prev_s

        elif prev_s == curr_s and prev_e < curr_e:
            curr_length = curr_e - curr_s + 1
            prev_e = curr_e
            prev_s = prev_s

        elif prev_s == curr_s and prev_e > curr_e:
            curr_length = prev_e - curr_e + 1
            prev_e = prev_e
            prev_s = curr_e

        elif prev_s == curr_s and prev_e == curr_e:
            curr_length = curr_e - curr_s + 1

    return curr_length


print(highlight())
