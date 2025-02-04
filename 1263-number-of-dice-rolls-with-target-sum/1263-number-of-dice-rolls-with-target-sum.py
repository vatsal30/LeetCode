class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = (10 ** 9) + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(n):
            new_dp = [0] * (target + 1)
            
            for val in range(1, k + 1):
                for total in range(val, target + 1):
                    new_dp[total] = (new_dp[total] + dp[total - val]) % mod
            dp = new_dp
        return dp[target]