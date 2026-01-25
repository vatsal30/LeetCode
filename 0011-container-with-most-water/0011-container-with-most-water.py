class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        idx1 = 0
        idx2 = len(height) - 1

        while idx1 < idx2:
            ans = max(ans, min(height[idx1], height[idx2]) * (idx2 - idx1))
        
            if height[idx1] < height[idx2]:
                idx1 += 1
            else:
                idx2 -= 1
        return ans