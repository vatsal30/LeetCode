#User function Template for python3

from typing import List
from collections import deque

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        q = deque()
        vis = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            if(not vis[i][0] and grid[i][0] == 1):
                q.append((i, 0))
                vis[i][0] = 1
            if(not vis[i][m-1] and grid[i][m-1] == 1):
               q.append((i, m-1))
               vis[i][m-1] = 1
        
        for j in range(m):
            if(not vis[0][j] and grid[0][j] == 1):
                q.append((0, j))
                vis[0][j] = 1
            if(not vis[n-1][j] and grid[n-1][j] == 1):
                q.append((n-1, j))
                vis[n-1][j] = 1
        
        while q:
            row, col = q.popleft()
            delRow = [-1, 0, 1, 0]
            delCol = [0, -1, 0, 1]
            
            for i in range(4):
                nRow = row + delRow[i]
                nCol = col + delCol[i]
                
                if (nRow>=0 and nRow<n and nCol>=0 and nCol<m and (not vis[nRow][nCol]) and grid[nRow][nCol]==1):
                    q.append((nRow, nCol))
                    vis[nRow][nCol] = 1
        cnt = 0
        for i in range(n):
            for j in range(m):
                if(not vis[i][j] and grid[i][j]==1):
                    cnt += 1
        
        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends