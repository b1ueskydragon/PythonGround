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

        if e + 1 < len(ls[i]):
            nxt = (ls[i][e + 1], i, e + 1)
            heapq.heappush(heap, nxt)

    return res


given = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
print(solve(given))
