#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, row, col, grid, vis, vec, row0, col0):
        vis[row][col] = 1
        vec.append((row - row0, col - col0))
        
        n = len(grid)
        m = len(grid[0])
        
        delRow = [-1, 0, 1, 0]
        delCol = [0, -1, 0, 1]
        
        for i in range(4):
            nRow = row + delRow[i]
            nCol = col + delCol[i]
            
            if (nRow>=0 and nRow<n and nCol>=0 and nCol<m and not vis[nRow][nCol] and grid[nRow][nCol]==1):
                self.dfs(nRow, nCol, grid, vis, vec, row0, col0)
                
        
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        
        vis = [[0 for i in range(m)] for j in range(n)]
        st = set()
        for i in range(n):
            for j in range(m):
                if (not vis[i][j] and grid[i][j] == 1):
                    vec = []
                    self.dfs(i, j, grid, vis, vec, i, j)
                    st.add(tuple(vec))
        
        return len(st)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends