"""
KMP - partial match table

ABABC
 ABABC

A B A B C
0 0

ABABC
  ABABC

A B A B C
0 0 1 2

* shift 2 bits
ABABC
    ABABC

A B A B C
0 0 1 2 0

"""


def skip_table(pattern):
    """
    O(k)
      - k is the length of the pattern
    """
    matcher = [0] * len(pattern)

    pos = 0  # starting index of pattern
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[pos]:
            pos += 1
            matcher[i] = pos

        else:
            while pos != 0:
                pos = matcher[pos - 1]
            matcher[i] = 0

    return matcher


print(skip_table(pattern="ABABC"))


def search(string, pattern):
    matcher = skip_table(pattern)

    s, p = 0, 0  # cursor of string, pattern
    while s < len(string):
        if string[s] == pattern[p]:
            s += 1
            p += 1

            if p == len(pattern):
                return s - p

        else:
            p = matcher[p]  # restart position
