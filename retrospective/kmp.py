"""
[[ Partial match table ]]
Times : O(k)
        k is len(pattern)
"""


def partial_match_table(word, word_size):
    table = [0] * (word_size + 1)
    table[0] = -1
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


pattern = "ABABC"
print(partial_match_table(pattern, len(pattern)))
