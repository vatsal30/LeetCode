class Solution:
    def check(self, color, adj, start):
        queue = deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            for adj_node in adj[node]:
                if (color[adj_node] == -1):
                    color[adj_node] = (color[node] + 1) % 2
                    queue.append(adj_node)
                elif color[adj_node] == color[node]:
                    return False
        return True
            
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for node in range(n):
            if color[node] == -1:
                if not self.check(color, graph, node):
                    return False
        return True