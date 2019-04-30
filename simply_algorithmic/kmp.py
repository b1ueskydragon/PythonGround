"""
[[ Partial match table ]]
Times : O(k)
        k is len(pattern)
"""


# TODO: fix bug?
def partial_match_table_for(word, word_size):
    table = [0] * word_size
    w = 0  # current lookup position in table

    for t in range(1, word_size):
        if word[w] == word[t]:
            w += 1
            table[t] = w
        else:
            # i = 0
            while w != 0:
                w = table[w - 1]
            table[t] = 0

    return table


def partial_match_table_while(word, word_size):
    table = [0] * (word_size + 1)
    table[0] = -1  # sentinel
    w, t = 0, 1

    while t < word_size:
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


pattern = "ina, iina"
print(partial_match_table_for(pattern, len(pattern)))
print(partial_match_table_while(pattern, len(pattern)))
