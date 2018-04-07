# current length with space (list-len)
def curr_len(words):
    return sum(len(word) for word in words) + len(words) - 1

def break_text(s, k):
    words = s.split(' ')
    tmp = []
    result = []
    for i, word in enumerate(words):
        if curr_len(tmp + [word]) <= k:
            tmp.append(word)
        else:
            result.append(tmp)
            tmp = [word]

    return result + [tmp]


text = "the quick brown fox jumps over the lazy dog"
print(break_text(text, 10))
