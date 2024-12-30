class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * high
        for idx in range(1, high + 1):
            if idx >= zero:
                dp[idx] += dp[idx - zero]
            if idx >= one:
                dp[idx] += dp[idx - one]
            dp[idx] = dp[idx] % mod
        return sum(dp[low: high + 1])% mod