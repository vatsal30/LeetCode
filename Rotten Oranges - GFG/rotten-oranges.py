class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
        n = len(grid)
        m = len(grid[0])
        queue = []
        vis = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 2):
                    queue.append([(i, j), 0])
                    vis[i][j] = 2
        
        time = 0
        deltaRow = [-1, 0 , 1, 0]
        deltaCol = [ 0, 1, 0, -1]
        while queue:
            temp = queue.pop(0)
            row, col = temp[0]
            t = temp[1]
            time = max(t, time)
            for i in range(4):
                nRow = row + deltaRow[i]
                nCol = col + deltaCol[i]
                if (nRow>=0 and nRow<n and nCol>=0 and nCol<m and vis[nRow][nCol]!=2 and grid[nRow][nCol]==1):
                    queue.append([(nRow, nCol), t+1])
                    vis[nRow][nCol] = 2
        
        for i in range(n):
            for j in range(m):
                if (vis[i][j]!=2 and grid[i][j]==1):
                    return -1
        
        return time
                

#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends