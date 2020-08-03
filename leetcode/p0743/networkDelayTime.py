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

        for k in itinerary:  # sort by time it takes (w).
            itinerary[k] = sorted(itinerary[k], key=lambda pair: pair[1])

        time_to_reach = {node: float('inf') for node in range(1, N + 1)}

        #  take for all nodes (broadcast from the root node).
        def find(start, acc):
            if acc >= time_to_reach[start]:
                # since it's sorted by time (w) already. We should take shorter one.
                return
            time_to_reach[start] = acc
            if start not in itinerary:
                return
            for candidate in itinerary[start]:
                v, w = candidate[0], candidate[1]
                find(v, acc + w)

        find(K, 0)
        res = max(time_to_reach.values())  # if there is any non-visited node, inf will remain.
        return (res, -1)[res == float('inf')]
