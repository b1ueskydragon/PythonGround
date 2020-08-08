from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        itinerary = dict()
        for time in times:
            u, v, w = time[0], time[1], time[2]
            if u in itinerary:
                itinerary[u].append((v, w))
            else:
                itinerary[u] = [(v, w)]

        sent = [False] * (N + 1)
        time_to_reach = {node: float('inf') for node in range(1, N + 1)}
        time_to_reach[K] = 0  # start point

        while True:
            curr_node = -1  # start point
            curr_elapsed = float('inf')

            for node in range(1, N + 1):  # find non-visited node which might be a current start point
                if not sent[node] and time_to_reach[node] < curr_elapsed:
                    curr_node = node
                    curr_elapsed = time_to_reach[node]

            if curr_node == -1:  # all nodes are visited
                break

            sent[curr_node] = True
            if curr_node not in itinerary:
                continue
            for neighbour in itinerary[curr_node]:
                v, w = neighbour
                time_to_reach[v] = min(time_to_reach[v], curr_elapsed + w)

        res = max(time_to_reach.values())
        return res if res < float('inf') else -1
