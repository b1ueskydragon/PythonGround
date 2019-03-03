from collections import deque


def bfs(start, goal):
    previous = {}
    found = deque()
    current = None

    previous[start] = None
    found.append(start)

    while found and current != goal:
        current = found.pop()
        for st in current:  # TODO
            if st not in found:
                found.append(st)
                previous[st.name] = st

    if current == goal:
        return previous
    else:
        return None
