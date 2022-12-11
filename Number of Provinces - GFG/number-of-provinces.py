#User function Template for python3
from collections import defaultdict
class Solution:
    
    def dfs(self, node, adjL, vis):
        vis[node] = 1
        for i in adjL[node]:
            if (vis[i] != 1):
                self.dfs(i, adjL, vis)
        
    def numProvinces(self, adj, V):
        # code here 
        adjL = defaultdict(list)
        for i in range(len(adj)):
            for j in range(len(adj[0])):
                if (adj[i][j] == 1 and i!=j):
                    adjL[i].append(j)

        vis = [0 for i in range(V)]
        provinces = 0
        
        for i in range(V):
            if(vis[i] != 1):
                provinces += 1
                self.dfs(i, adjL, vis)
        return provinces
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends