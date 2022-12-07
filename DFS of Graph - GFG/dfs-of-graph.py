#User function Template for python3

class Solution:
    
    def dfs (self, node, adj, visited, dfsList):
        visited[node] = 1
        dfsList.append(node)
        
        for i in adj[node]:
            if visited[i] == 0:
                self.dfs(i, adj, visited, dfsList)
        
        return dfsList

    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [0 for i in range(V)]
        dfsList = []
        
        self.dfs(0, adj, visited, dfsList)
        
        return dfsList

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends