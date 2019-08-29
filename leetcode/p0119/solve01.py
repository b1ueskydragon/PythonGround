"""
use deque, since it provides pop or append both end efficiently.
"""
from collections import deque

prev_res = [1, 6, 15, 20, 15, 6, 1]
k = 7  # k of current res

queue = deque(prev_res)

acc = 0
while k:
    curr = queue.popleft()
    queue.append(acc + curr)
    acc = curr
    k -= 1

queue.append(1)

print(list(queue))  # [1, 7, 21, 35, 35, 21, 7, 1]
