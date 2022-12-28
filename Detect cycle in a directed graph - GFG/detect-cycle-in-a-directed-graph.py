#User function Template for python3


class Solution:
    
    def dfs(self, node, V, adj, vis, path):
        vis[node] = 1
        path[node] = 1
        
        for i in adj[node]:
            if vis[i]==0:
                if self.dfs(i, V, adj, vis, path):
                    return True
            elif path[i]==1:
                return True
        
        path[node] = 0
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis = [0 for i in range(V)]
        path = [0 for i in range(V)]
        for i in range(V):
            if (vis[i]==0):
                if (self.dfs(i, V, adj, vis, path)):
                    return True
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends