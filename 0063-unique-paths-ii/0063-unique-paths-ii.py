class Solution:
    def dfs(self, i, j, dp, grid):
        if grid[i][j] == 1:
            return 0
        if (i, j) == (0, 0):
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 0
        if i-1 >= 0:
            ans += self.dfs(i-1, j, dp, grid) 
        if j -1 >= 0:
            ans += self.dfs(i, j - 1, dp, grid)
        dp[i][j] = ans
        return ans 
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)] 
        # dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             continue
        #         if obstacleGrid[i][j] == 1:
        #             dp[i][j] = 0
        #             continue
        #         up = 0
        #         if i > 0:
        #             up = dp[i-1][j]
        #         left = 0
        #         if j > 0:
        #             left = dp[i][j-1]
        #         dp[i][j] = up + left
        # return dp[m-1][n-1]
        return self.dfs(m-1, n-1, dp, obstacleGrid)