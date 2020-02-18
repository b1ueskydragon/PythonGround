class Solution:
    def __init__(self):
        self.terminals = set()
        self.visitedRoots = set()  # overall

    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        self.terminals = {node for node, end_points in enumerate(graph) if not end_points}
        return [node for node, _ in enumerate(graph) if self.is_terminal_node(graph, node, set())]

    def is_terminal_node(self, graph, start, visited):
        if start in self.terminals:
            return True
        if start in self.visitedRoots:
            return False
        if start in visited:
            return False
        visited.add(start)  # during the specific start point
        for step in graph[start]:
            if self.is_terminal_node(graph, step, visited):
                self.terminals.add(step)
            else:
                self.visitedRoots.add(start)
                visited.add(step)
                return False
        return True
