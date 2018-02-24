# should be O(N)
def longest_substring(s, k):
    if k >= len(s):
        return s

    # init settings
    k_set = set(s[0])
    buff = [s[0]]
    i = 1
    mark = buff[0]  # element which remove from set
    pu = '#'  # punctuation

    table = {s[0] : 1}

    while i <= len(s) - 1:
        current_look = s[i]
        k_set.add(current_look)

        if current_look in table:
            table.update({current_look: table.get(current_look) + 1})
        else:
            table.update({current_look: 1})

        if len(k_set) > k:
            k_set.discard(mark)

            end_point_value = buff[-1]

            buff.append(pu)

            buff.append(end_point_value)

            buff.append(current_look)

            mark = end_point_value
        else:
            buff.append(current_look)

        i += 1

    result = "".join(buff).split(pu)

    return buff


s = "aababcc"
k = 2

print(longest_substring(s, k))
