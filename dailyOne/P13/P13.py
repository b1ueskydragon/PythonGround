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

    while i <= len(s) - 1:
        current_look = s[i]
        k_set.add(current_look)

        if len(k_set) > k:
            k_set.discard(mark)
            is_adjacent_same = buff[-1] == buff[-2]
            after_pu = buff[-1]
            buff.append(pu) # TODO 同じ数列くっつける必要あり start, end
            buff.append(after_pu)
            buff.append(current_look)
            mark = after_pu
        else:
            buff.append(current_look)

        i += 1

    result = "".join(buff).split(pu)

    return buff


s = "aabbccddd"
k = 2

print(longest_substring(s, k))
