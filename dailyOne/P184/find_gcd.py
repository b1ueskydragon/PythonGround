"""
Given n numbers, find the greatest common denominator between them.
"""


def find_gcd(given):
    """
    reducing (folding)
    """
    head = given[0]
    for _ in given[1:]:
        head = gcd(head, _)
    return head


def gcd(a, b):
    if b is 0:
        return abs(a)
    return gcd(b, a % b)


given = [42, 56, 14, 21]
print(find_gcd(given))
