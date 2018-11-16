def retrieval(word, patt):
    """
    less than O(N * k) worst time.

    :param word: string
    :param patt: pattern
    :return: Start index if pattern found, else False.
    """
    k = len(patt)
    word += patt  # sentinel

    j = 0

    for i, char in enumerate(word):
        if i == len(word):
            return -1

    return -1


# Think a goal first what should I do with given conditions.
print(retrieval("retrieval", "trie"))  # 2
print(retrieval("retrieval", "e"))  # 1
