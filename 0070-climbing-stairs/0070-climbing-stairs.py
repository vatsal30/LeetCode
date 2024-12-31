class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            if i >= 2:
                dp[i] += dp[i-2]
            dp[i] += dp[i-1]
        return dp[-1]