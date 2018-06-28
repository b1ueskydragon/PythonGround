"""
two elements appear exactly once and all other elements appear exactly twice.
find the two elements that appear only once.

order does not matter.
in linear time and constant space.
"""


def find_two_once(ary):
    """
    over constant space edition.
    grows in size with the number of unique elements.
    """
    table = set()

    for k in ary:
        be = len(table)
        table.add(k)
        af = len(table)
        if be is af:
            table.remove(k)
    return table


# given = [2, 4, 6, 8, 10, 2, 6, 10]
print(find_two_once([int(input()) for _ in range(int(input()))]))
