class Solution:
    def __init__(self):
        self.res = set()
        self.visited = set()

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        for node, end_points in enumerate(graph):
            if node not in self.visited:
                self.is_terminal_node(node, graph)
        return sorted(self.res)

    def is_terminal_node(self, start, graph):
        if start in self.res:
            return True
        if start in self.visited:
            return False
        self.visited.add(start)
        for step in graph[start]:
            if not self.is_terminal_node(step, graph):
                return False
        self.res.add(start)
        return True
