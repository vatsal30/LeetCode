class Solution:
    def dfs(self, i, j, dp):
        if (i, j) == (0, 0):
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 0
        if i-1 >= 0:
            ans += self.dfs(i-1, j, dp) 
        if j -1 >= 0:
            ans += self.dfs(i, j - 1, dp)
        dp[i][j] = ans
        return ans 
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)] 
        return self.dfs(m-1, n-1, dp)