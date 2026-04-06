import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / mid)
            if cnt > h:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans 