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

    cnt = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[cnt]:
            cnt += 1
            matcher[i] = cnt

        else:
            while cnt != 0:
                cnt = matcher[cnt - 1]
            matcher[i] = 0

    return matcher


print(skip_table(pattern="ABABC"))
