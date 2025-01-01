class Solution:
    def dfs(self, idx, dp, nums):
            if idx == 0:
                dp[idx] = nums[idx]
                return nums[idx]
            if idx < 0:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            left = self.dfs(idx-2, dp, nums) + nums[idx]
            right = self.dfs(idx-1, dp, nums)
            dp[idx] = max(left, right)
            return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        adj_house = nums[0]
        non_adj = 0
        for i in range(1, n):
            pick = nums[i] + non_adj
            not_pick = adj_house
            curr_pick = max(pick, not_pick)
            non_adj = adj_house
            adj_house = curr_pick
        return adj_house