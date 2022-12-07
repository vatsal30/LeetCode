#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        bfsList = []
        visited = [0 for i in range(V)]
        queue = []
        
        queue.append(0)
        visited[0] = 1
        
        while queue:
            node = queue.pop(0)
            bfsList.append(node)
            for vertex in adj[node]:
                if (visited[vertex] == 0):
                    visited[vertex] = 1
                    queue.append(vertex)
        
        return bfsList


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends