#User function Template for python3
from collections import deque 

class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        adj = [[] for i in range(N)]
        
        for start, end in prerequisites:
            adj[start].append(end)
        
        indegree = [0 for i in range(N)]
        for i in range(N):
            for node in adj[i]:
                indegree[node] += 1
        
        que = deque()
        
        for i in range(N):
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
        
        if (cnt == N): return True
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends