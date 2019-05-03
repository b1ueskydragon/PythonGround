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
    table = partial_match_table(word)
    i, p = 0, 0  # cursor of text, word

    while i != len(text) and p != len(word):
        if text[i] == word[p]:  # index `i` only go forward, not backward
            i += 1
            p += 1
        elif p == 0:  # not matched and there is no skip
            i += 1
        else:  # set restart position
            p = table[p]

    return (-1, i - p)[p == len(word)]
