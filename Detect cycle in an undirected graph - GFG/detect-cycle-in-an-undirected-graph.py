
from typing import List
class Solution:
    
    def detect(self, start, adj, vis):
        vis[start] = 1
        queue = []
        queue.append((start, -1))
        while queue:
            currNode, parent = queue.pop(0)
            adjNodes = adj[currNode]
            
            for node in adjNodes:
                if(vis[node]==0):
                    queue.append((node, currNode))
                    vis[node] = 1
                elif(node!=parent):
                    return True
        return False
            
            
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        vis = [0 for i in range(V)]
        for i in range(V):
            if (vis[i] == 0):
                if (self.detect(i, adj, vis)):
                    return True
        
        return False

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends