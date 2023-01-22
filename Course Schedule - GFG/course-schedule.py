#User function Template for python3
from collections import deque
class Solution:
    def findOrder(self, N, m, prerequisites):
        # Code here
        adj = [[] for i in range(N)]
        
        for start, end in prerequisites:
            adj[end].append(start)
        
        indegree = [0 for i in range(N)]
        for i in range(N):
            for node in adj[i]:
                indegree[node] += 1
        
        que = deque()
        
        for i in range(N):
            if indegree[i] == 0:
                que.append(i)
        
        ans = []
        
        while que:
            node = que.popleft()
            ans.append(node)
            for ele in adj[node]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    que.append(ele)
        
        if (len(ans) == N): return ans
        
        return []

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends