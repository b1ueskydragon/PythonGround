"""
[[ Partial match table ]]
Times : O(k)
        k is len(pattern)
"""


def partial_match_table(word):
    table = [0] * (len(word) + 1)
    table[0] = -1
    w, t = 0, 1

    while t < len(word):
        if word[w] == word[t]:  # sub-pattern found
            w += 1
            t += 1
            table[t] = w
        elif w > 0:  # no sub-pattern, fallback
            w = table[w]
        else:  # w == 0
            t += 1
            table[t] = 0

    return table


def kmp_search(text, word):
    table = partial_match_table(word)

    t, w = 0, 0  # cursor of text, word
    while t != len(text) and w != len(word):
        if text[t] == word[w]:  # index `t` only go forward, not backward
            t += 1
            w += 1
        elif w == 0:  # not matched and there is no skip
            t += 1
        else:  # set restart position
            w = table[w]

    if w == len(word):  # cursor is on end
        return t - w  # end pos - start pos

    return -1
