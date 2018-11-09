# https://beta.atcoder.jp/contests/arc103/tasks/arc103_a

"""
improvement space - more less variables
            time  - use collections, avoid using list length or for-loop
"""

from collections import Counter


def solve(size=int(input()), ary=list(map(int, input().split()))):
    even, odd = Counter(ary[::2]), Counter(ary[1::2])
    """ 
    put a sentinel in counter - make elements more than one always.
    avoid error when given was only one element - e. g.) [1, 1, 1, 1]
    given value should be bigger than 1 - so we put 0 count to 0.
    """
    even[0], odd[0] = 0, 0
    (e, em), (_, es) = even.most_common(2)
    (o, om), (_, os) = odd.most_common(2)
    return size - max(em + os, es + om) if e == o else size - em - om


print(solve())
