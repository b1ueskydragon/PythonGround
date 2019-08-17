import random

"""
Fisher–Yates shuffle - Algorithm P
"""


def algorithm_p(given):
    size = len(given)
    for i, _ in enumerate(reversed(range(size))):
        j = random.randrange(size)  # or (0, given[-1])
        given[i], given[j] = given[j], given[i]

    return given


given = [int(input()) for i in range(int(input()))]
print(given)
print(algorithm_p(given))
