class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        buy = prices[0]
        n = len(prices)
        for i in range(1, n):
            if buy < prices[i]:
                ans += (prices[i] - buy)
                buy = prices[i]
            elif prices[i] < buy:
                buy = prices[i]

        return ans
            