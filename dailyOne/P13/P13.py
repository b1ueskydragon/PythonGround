# should be O(N)
def longest_substring(str, kth):
    if kth >= len(str):
        return str

    for i, v in enumerate(str, kth):
        candidate = str[:kth]
        candidate += str[i]
        s = set(candidate)
        if len(s) < kth:
            candidate += str[i]
        else:
            candidate = str[i - 1:]

    return candidate


s = "abcba"
k = 2

print(longest_substring(s, k))
