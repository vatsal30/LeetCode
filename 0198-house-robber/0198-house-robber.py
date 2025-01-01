class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dfs(idx):
            if idx == 0:
                dp[idx] = nums[idx]
                return nums[idx]
            if idx < 0:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            left = dfs(idx-2) + nums[idx]
            right = dfs(idx-1)
            dp[idx] = max(left, right)
            return dp[idx]
        dfs(n-1)
        return dp[n-1]