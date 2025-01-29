class DSU:
	def __init__(self, vertices: int):
		 self.n = vertices
		 self.size = [1] * vertices
		 self.parent = list(range(vertices))

	def find_set(self, node: int) -> int:
		if self.parent[node] == node:
			return node
		self.parent[node] = self.find_set(self.parent[node])
		return self.parent[node]

	def union_set(self, nodeOne: int, nodeTwo: int) -> bool:
		nodeOne = self.find_set(nodeOne)
		nodeTwo = self.find_set(nodeTwo)
		if nodeOne == nodeTwo:
			return True
		else:
			if self.size[nodeOne] > self.size[nodeTwo]:
				self.parent[nodeTwo] = nodeOne
				self.size[nodeOne] += self.size[nodeTwo]
			else:
				self.parent[nodeOne] = nodeTwo
				self.size[nodeTwo] += self.size[nodeOne]
		return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union = DSU(n)
        for edge in edges:
            if union.union_set(edge[0] - 1, edge[1] - 1):
                return edge
        return []
        