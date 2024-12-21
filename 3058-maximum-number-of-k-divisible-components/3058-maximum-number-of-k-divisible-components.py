from collections import defaultdict, deque

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        ans = 1
        if n < 2:
            return ans
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        queue = deque()
        for node, leafs in graph.items():
            if len(leafs) == 1:
                queue.append(node)
        while queue:
            node = queue.popleft()
            neighbor_node = graph[node][0] if len(graph[node]) > 0 else -1
            
            if neighbor_node == -1:
                continue
            if values[node] % k == 0:
                ans += 1
            else:
                values[neighbor_node] += values[node]
            graph[neighbor_node].remove(node)
            if len(graph[neighbor_node]) == 1:
                queue.append(neighbor_node)
        return ans