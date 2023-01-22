#User function Template for python3

from typing import List
from collections import deque
class Solution:    
    
    # Using DFS
    # def dfs(self, node, adj, vis):
    #     vis[node] = 2

    #     for i in adj[node]:
    #         if (vis[i] == 0):
    #             if self.dfs(i, adj, vis):
    #                 return True
    #         elif (vis[i] == 2):
    #             return True
        
    #     vis[node] = 1
        
    #     return False
                    
    # def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
    #     # code here
    #     vis = [0 for i in range(V)]

    #     for i in range(V):
    #         if vis[i] == 0:
    #             self.dfs(i, adj, vis)
        
    #     ans = []
    #     for i in range(V):
    #         if vis[i] == 1:
    #             ans.append(i)
        
    #     return ans
    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        
        adjRev = [[] for i in range(V)]
        indegree = [0 for i in range(V)]
        for i in range(V):
            for node in adj[i]:
                adjRev[node].append(i)
                indegree[i]+=1
        
        que = deque()
        
        for i in range(V):
            if indegree[i]==0:
                que.append(i)
        
        ans = []
        while que:
            node = que.popleft()
            ans.append(node)
            
            for i in adjRev[node]:
                indegree[i]-=1
                if(indegree[i] == 0):
                    que.append(i)
        ans.sort()
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends