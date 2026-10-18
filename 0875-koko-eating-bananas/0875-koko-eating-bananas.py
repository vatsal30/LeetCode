class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            cnt = sum((pile + mid - 1) // mid for pile in piles)
            if cnt <= h:
                right = mid
            else:
                left = mid + 1
        return left