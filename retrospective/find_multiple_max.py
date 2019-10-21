"""
Pick three numbers in an list, find a maximum multiple result.
if the list size is lower than 3, return -1.
zero or negative numbers are may be included.
"""

from heapq import heappush, heappop


# heapify for pop with order by asc
def solve(xs):
    if len(xs) < 3:
        return -1
    hq = reversed_heapify(xs)
    return -1 * heappop(hq) * heappop(hq) * heappop(hq)


def reversed_heapify(xs):
    hq = []
    for x in xs:
        heappush(hq, x * -1)
    return hq
