def solve(string):
    words = string.split()
    max_len = 0
    for word in words:
        max_len = max(max_len, len(word))
    return max_len


def solve_(string):
    from functools import reduce
    return reduce(max, map(len, string.split()))
