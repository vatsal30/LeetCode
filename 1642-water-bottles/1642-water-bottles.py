class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        while numBottles:
            ans += numBottles
            tmp = numBottles + empty
            numBottles = tmp // numExchange
            empty = tmp % numExchange
        return ans
            