class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        firstSum = sum(grid[0])
        secondSum = 0
        ans = float("inf")
        for t_idx in range(len(grid[0])):
            firstSum -= grid[0][t_idx]
            ans = min(ans, max(firstSum, secondSum))
            secondSum += grid[1][t_idx]
        return ans