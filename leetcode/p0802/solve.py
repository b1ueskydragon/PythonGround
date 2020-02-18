class Solution:
    def __init__(self):
        self.res = []
        # self.visited = set()  # overall

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        for node, _ in enumerate(graph):
            if self.has_terminal_node(graph, node, set()):
                self.res.append(node)
        return self.res

    def has_terminal_node(self, graph, start, visited):
        end_points = graph[start]
        if not end_points:  # a terminal node
            return True
        if start in visited:
            return False
        visited.add(start)  # at a specific start point
        for step in end_points:
            if not self.has_terminal_node(graph, step, visited):
                return False
        return True
