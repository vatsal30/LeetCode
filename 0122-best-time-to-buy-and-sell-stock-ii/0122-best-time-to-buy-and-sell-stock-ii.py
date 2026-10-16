class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i-1] < prices[i]:
                ans += (prices[i] - prices[i-1])
                buy = prices[i]

        return ans
            