from collections import deque


def bfs(start, goal):
    memo = {}  # mapping station -> prev (どこから来たか)
    lookup = deque()  # lookup 予定の待ち¬列
    current = None

    memo[start] = current
    lookup.append(start)

    while lookup and current != goal:
        current = lookup.popleft()
        for st in current.neighbors:
            if st not in memo.keys():
                lookup.append(st)
                memo[st] = current

    if current == goal:
        path = [goal]
        curr = goal

        while memo[curr]:
            curr = memo[curr]
            path.append(memo[curr])

        return path
