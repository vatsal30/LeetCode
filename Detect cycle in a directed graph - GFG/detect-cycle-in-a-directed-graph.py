#User function Template for python3

from collections import deque
class Solution:
    
    # using DFS
    # def dfs(self, node, V, adj, vis):
    #     vis[node] = 2
        
    #     for i in adj[node]:
    #         if vis[i]==0:
    #             if self.dfs(i, V, adj, vis):
    #                 return True
    #         elif vis[i]==2:
    #             return True
        
    #     vis[node] = 1
    #     return False
    
    # #Function to detect cycle in a directed graph.
    # def isCyclic(self, V, adj):
    #     # code here
    #     vis = [0 for i in range(V)]
    #     for i in range(V):
    #         if (vis[i]==0):
    #             if (self.dfs(i, V, adj, vis)):
    #                 return True
        
    #     return False
    
    
    # Using BFS Kahn's algo
    def isCyclic(self, V, adj):
        indegree = [0 for i in range(V)]
        for i in range(V):
            for node in adj[i]:
                indegree[node] += 1
        
        que = deque()
        
        for i in range(V):
            if indegree[i] == 0:
                que.append(i)
        
        cnt = 0
        
        while que:
            node = que.popleft()
            cnt += 1
            for ele in adj[node]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    que.append(ele)
        
        if (cnt == V): return False
        
        return True
    

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