class Solution:
    def buildAdjList(self, edges):
        tree = defaultdict(list)
        for node1, node2 in edges:
            tree[node2].append(node1)
            tree[node1].append(node2)
        return tree
    
    def findFarthestNode(self, tree, len_tree, node):
        queue = deque()
        queue.append((node, 0))
        visited = [False] * len_tree
        farthest_node = node
        distance = 0
        while queue:
            n1, dist = queue.popleft()
            distance = dist
            farthest_node = n1
            if not visited[n1]:
                visited[n1] = True
                for n2 in tree[n1]:
                    queue.append((n2, dist+1))

        return farthest_node, distance


    def findDiameter(self, tree, len_tree):
        farthestNode, _ = self.findFarthestNode(tree, len_tree, 0)
        _, distance = self.findFarthestNode(tree, len_tree, farthestNode)
        return distance
        
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1) + 1
        m = len(edges2) + 1
        tree1 = self.buildAdjList(edges1)
        tree2 = self.buildAdjList(edges2)
        diameter1 = self.findDiameter(tree1, n)
        diameter2 = self.findDiameter(tree2, m)
        return max(diameter1, diameter2, ceil(diameter1/2) + ceil(diameter2/2)+ 1)
        