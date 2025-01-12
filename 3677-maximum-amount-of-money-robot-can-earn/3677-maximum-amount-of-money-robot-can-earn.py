class Solution:

    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[float("-inf")]*3 for _ in range(n)] for _ in range(m)]
        for k in range(3):
            dp[0][0][k] = coins[0][0] if coins[0][0] >= 0 else (0 if k > 0 else coins[0][0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                for k in range(3):
                    if i > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + coins[i][j])
                    if j > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + coins[i][j])

                    if coins[i][j] < 0 and k > 0:
                        if i > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                        if j > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        return max(dp[m-1][n-1])
                            
                    
                        
        
        