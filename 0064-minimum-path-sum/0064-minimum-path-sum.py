class Solution:
    def dfs(self, i, j, dp, grid):
        if (i, j) == (0, 0):
            return grid[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        up = float("inf")
        if i-1 >= 0:
            up = self.dfs(i-1, j, dp, grid) 
        down = float("inf")
        if j -1 >= 0:
            down = self.dfs(i, j - 1, dp, grid)
        dp[i][j] = grid[i][j] + min(up, down)
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)] 
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                up = float("inf")
                if i > 0:
                    up = dp[i-1][j]
                left = float("inf")
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = grid[i][j] + min(up, left)
        return dp[m-1][n-1]
        # return self.dfs(m-1, n-1, dp, grid)