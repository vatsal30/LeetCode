class Solution:
    def dfs(self, houses):
        adj_house = houses[0]
        non_adj = 0
        for i in range(1, len(houses)):
            curr_pick = max(non_adj + houses[i], adj_house)
            non_adj = adj_house
            adj_house = curr_pick
        return adj_house

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        return max(self.dfs(nums[:-1]), self.dfs(nums[1:]))
