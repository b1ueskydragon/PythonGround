class Solution:
    def __init__(self):
        self.res = []
        self.terminals = set()
        # self.visited = set()  # overall

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        self.terminals = {node for node, end_points in enumerate(graph) if not end_points}
        for node, _ in enumerate(graph):
            if self.has_terminal_node(graph, node, set()):
                self.res.append(node)
        return self.res

    def has_terminal_node(self, graph, start, visited):
        if start in self.terminals:  # since this a terminal node
            return True
        if start in visited:
            return False
        visited.add(start)  # during the specific start point
        for step in graph[start]:
            if self.has_terminal_node(graph, step, visited):
                self.terminals.add(step)
            else:
                return False
        return True
