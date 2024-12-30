class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for idx, price in enumerate(prices):
            j = idx + 1
            while j < len(prices) and prices[j] > price:
                j += 1
            if j == len(prices):
                ans.append(price)
            else:
                ans.append(price - prices[j])
        return ans