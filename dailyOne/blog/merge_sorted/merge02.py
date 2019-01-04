"""
with heap
"""
import heapq


def solve(ls, res=[]):
    heap = [(l[0], i, 0) for i, l in enumerate(ls) if l]
    heapq.heapify(heap)

    while heap:
        v, i, e = heapq.heappop(heap)
        res.append(v)

        en = e + 1
        if en < len(ls[i]):
            heapq.heappush(heap, (ls[i][en], i, en))

    return res


given = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print(solve(given))
