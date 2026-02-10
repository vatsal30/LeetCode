class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy_i = 0
        sell_i = 1
        if (len(prices) == 1):
            return 0
        while(sell_i < len(prices)):
            profit = prices[sell_i] - prices[buy_i]
            if (profit > 0):
                if (max_p < profit):
                    max_p = profit
                sell_i += 1
            else:
                buy_i = sell_i
                sell_i += 1
                
            
        return max_p