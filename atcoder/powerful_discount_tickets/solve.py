from heapq import heapify, heappush, heappop

n, m = map(int, input().split())
A = list(map(lambda x: int(x) * -1, input().split()))
heapify(A)  # in-place

for _ in range(m):
    tmp = -1 * heappop(A)  # max
    heappush(A, -1 * (tmp // 2))  # heapified A only contains negative num

print(-sum(A))
