from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V = len(graph)
        outdegree = [0] * V
        reverse = [[] for _ in range(V)]
        for node in range(V):
            outdegree[node] = len(graph[node])
            for it in graph[node]:
                reverse[it].append(node)
        q = deque()
        for node, degree in enumerate(outdegree):
            if degree == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            for parent in reverse[node]:
                outdegree[parent] -= 1
                if outdegree[parent] == 0:
                    q.append(parent)
            
        ans = []
        for node, degree in enumerate(outdegree):
            if degree == 0:
                ans.append(node)
        return ans
        