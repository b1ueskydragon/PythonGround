class Solution:
    def __init__(self):
        self.visited = set()
        self.res = set()  # TODO list with continue

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        for i, node in enumerate(graph):
            if not node:
                self.res.add(i)
            else:
                self.has_terminal_node(graph, i)
        return list(self.res)

    def has_terminal_node(self, graph, start):
        end_points = graph[start]
        if not end_points:
            return True
        for step in end_points:
            if step in self.visited:
                return False
            self.visited.add(step)
            if self.has_terminal_node(graph, step):
                self.res.add(step)
