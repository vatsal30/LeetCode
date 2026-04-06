import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            cnt = sum(math.ceil(pile / mid) for pile in piles)
            if cnt <= h:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans 