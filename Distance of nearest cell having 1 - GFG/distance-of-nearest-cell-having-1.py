from collections import deque
class Solution:
    
    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		#Code here
		n = len(grid)
		m = len(grid[0])
		
		vis = [[0] * m for _ in range(n)]
        result = [[0] * m for _ in range(n)]
        
        queue = deque()
        for i in range(n):
            for j in range(m):
                if (grid[i][j]==1):
                    vis[i][j] = 1
                    queue.append((i, j, 0))
        
        row_delta = [0, 0, -1, 1]
        col_delta = [-1, 1, 0, 0]

        while queue:
            row, col, dist =  queue.popleft()
            result[row][col] = dist
            
            for di, dj in zip(row_delta, col_delta):
                ni, nj = row + di, col + dj

                if (0 <= ni < n and 0 <= nj < m and vis[ni][nj] == 0):
                    vis[ni][nj] = 1
                    queue.append((ni, nj, dist + 1))
                
        return result
                
        

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends