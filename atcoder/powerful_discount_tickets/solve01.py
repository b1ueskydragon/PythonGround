from heapq import heappush, heappop

n, m = map(int, input().split())
A = input().split()
hq = []  # additional space
for a in A:
    heappush(hq, -1 * int(a))

for _ in range(m):
    tmp = -1 * heappop(hq)
    heappush(hq, -1 * (tmp // 2))

print(-sum(hq))
