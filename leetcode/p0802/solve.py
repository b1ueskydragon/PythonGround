class Solution:
    def __init__(self):
        self.visited = set()

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        safes = []
        for i, node in enumerate(graph):  # each node is a sorted list
            if node == []:
                safes.append(i)
            else:
                start_point = self.get_start_point(graph, i)
                if start_point:
                    safes.append(start_point)  # TODO: append a start point, not a final goal
        return safes

    def get_start_point(self, graph, pos):
        end_points = graph[pos]
        if end_points == []:
            return pos
        for point in end_points:
            print(self.visited)
            if point in self.visited:
                continue
            self.visited.add(pos)
            # TODO append condition
            # the result of retrieval of current end_point is not a circle

            # TODO not append condition
            # excepted above
            return self.get_start_point(graph, point)
