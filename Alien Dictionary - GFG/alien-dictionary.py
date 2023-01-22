#User function Template for python3
from collections import deque
class Solution:
    def topoSort(self, V, adj):
        indegree = [0 for i in range(V)]
        for i in range(V):
            for ele in adj[i]:
                indegree[ele]+=1
        
        que = deque()
        for i in range(V):
            if indegree[i]==0:
                que.append(i)
        ans = []
        while que:
            node = que.popleft()
            ans.append(node)
            
            for ele in adj[node]:
                indegree[ele] -= 1
                if indegree[ele]==0:
                    que.append(ele)
        return ans
        
    def findOrder(self,dict, N, K):
    # code here
        adj = [[] for i in range(K)]
        for i in range(N-1):
            s1 = dict[i]
            s2 = dict[i+1]
            min_len = min(len(s1), len(s2))
            for j in range(min_len):
                if(s1[j] != s2[j]):
                    adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                    break
            
        ans = self.topoSort(K, adj)
        ans_str = ''
        for i in ans:
            ans_str += chr(i + ord('a'))
        
        return ans_str

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends