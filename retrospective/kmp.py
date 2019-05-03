"""
[[ Partial match table ]]
Times : O(k)
        k is len(pattern)
"""


def partial_match_table(word):
    table = [0] * (len(word) + 1)
    table[0] = -1
    i, j = 0, 1

    while j < len(word):
        matched = word[i] == word[j]  # is sub pattern found

        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i

    return table


def kmp_search(text, word):
    skip_table = partial_match_table(word)

    t, w = 0, 0  # cursor of text, word
    while t != len(text) and w != len(word):
        if text[t] == word[w]:  # index `t` only go forward, not backward
            t += 1
            w += 1
        elif w == 0:  # not matched and there is no skip
            t += 1
        else:  # set restart position
            w = skip_table[w]

    if w == len(word):  # cursor is on end
        return t - w  # end pos - start pos

    return -1
