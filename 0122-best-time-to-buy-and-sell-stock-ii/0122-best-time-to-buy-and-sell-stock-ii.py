class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_i = 0
        curr_i = 1
        while (curr_i < len(prices)):
            if (prices[curr_i] > prices[buy_i]):
                if (prices[curr_i] > prices[curr_i - 1]):
                    curr_i +=1
                else:
                    max_profit += prices[curr_i-1] - prices[buy_i]
                    buy_i = curr_i
                    curr_i +=1
            else:
                if (buy_i != curr_i - 1):
                    max_profit += prices[curr_i-1] - prices[buy_i]
                buy_i = curr_i
                curr_i += 1
        if (buy_i != (curr_i-1)):
            max_profit += prices[curr_i - 1] - prices[buy_i]
        return max_profit