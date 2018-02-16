# head to tail
def count_decode(msg):
    if len(msg) == 0:  # basic case: ""
        return 1
    count = 0

    for i in [1, 2]:
        if i > len(msg):
            break
        head = msg[:i]
        tail = msg[i:]

        if head.startswith('0') or int(head) > 26:
            break
        count += count_decode(tail)

    return count


print(count_decode("111"))
print(count_decode("12345"))
print(count_decode("26"))
print(count_decode("27"), '\n')


# tail to head
def count_decode_later_parts(msg):
    buff = [0 for i in range(len(msg) + 1)]  # リスト内包記法

    buff[len(msg)] = 1  # base case: ""

    for i in reversed(range(len(msg))):  # reverse the list: the recurrence depends on the later parts of the structure
        for head_length in [1, 2]:  # head: 元のリストの tail 該当部分を先に計算
            if i + head_length > len(msg):
                break

            head = msg[i: i + head_length]
            if head.startswith('0') or int(head) > 26:
                break

            buff[i] += buff[i + head_length]

    return buff[0]


print(count_decode_later_parts("111"))
print(count_decode_later_parts("12345"))
print(count_decode_later_parts("26"))
print(count_decode_later_parts("27"), '\n')
