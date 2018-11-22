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
      - k is the length of the pattern.
    """
    matcher = [0] * len(pattern)  # list of restart position of each index in string

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
    """
    O(N)
      - N is the length of the string.
      - Make a huge skip range as much as possible.
        (with a partial match table)
    """
    matcher = skip_table(pattern)

    n, i = 0, 0  # cursor of string, pattern
    while n < len(string):
        if string[n] == pattern[i]:  # matched, go forward
            n += 1
            i += 1

            if i == len(pattern):  # pattern matched
                return n - i

        else:  # not matched, set restart position
            if i > 0:
                i = matcher[i - 1]
            else:  # head of string != head of pattern
                n += 1


print(search("ABABABABC", "ABABC"))
