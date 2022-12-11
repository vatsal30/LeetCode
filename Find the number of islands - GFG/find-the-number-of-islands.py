#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    
    def bfs(self, row, col, vis, grid):
        vis[row][col] = 1
        queue = []
        queue.append((row,col))
        row_c = len(grid)
        col_c = len(grid[0])
        
        while queue:
            row, col = queue.pop(0)
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    nrow = row + i
                    ncol = col + j
                    if (nrow>=0 and nrow<row_c and ncol>=0 and ncol<col_c and grid[nrow][ncol]==1 and vis[nrow][ncol]!=1):
                        vis[nrow][ncol] = 1
                        queue.append((nrow,ncol))
                        

    def numIslands(self,grid):
        #code here
        row_c = len(grid)
        col_c = len(grid[0])
        no_islands = 0
        
        vis = [[0 for j in range(col_c)] for i in range(row_c)]

        for row in range(row_c):
            for col in range(col_c):
                
                if (vis[row][col] != 1 and grid[row][col] == 1):
                    no_islands += 1
                    self.bfs(row, col, vis, grid)
        return no_islands
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
        print(obj.numIslands(grid))
# } Driver Code Ends