# TODO: More string-search algorithms (Boyer-Moore, Trie etc.)


def search(word, pattern):
    """
    less than O(N * k) worst time.

    N = len(string)
    k = len(pattern)

    :param word: string
    :param pattern: pattern
    :return: Start index if pattern found, else False.
    """
    p = 0

    word += pattern  # sentinel

    for i, char in enumerate(word):
        if p == len(pattern):
            return i - p

        if char == pattern[p]:
            p += 1
        else:
            p = 0

    return -1


# Think a goal first what should I do with given conditions.
print(search("retrieval", "trie"))  # 2
print(search("retrieval", "e"))  # 1
print(search("retrieval", "b"))  # -1
print(search("retrieval", "tria"))  # -1
print(search("retrieval", "l"))  # 8
print(search("retrievaltrivatrial", "tria"))  # 14

bigword = ''.join(["abcdeijklmnopqrtuvwxzghijklmnopqr"] * 100_000) + 's' + ''.join(['aabaa'] * 1_000) + 'f'
print(search(bigword, "f"))
print(search(bigword, "aab"))
print(search(bigword, "ba"))
print(search(bigword, "baa"))
