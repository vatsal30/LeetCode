class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        left, right = 0, len(height) - 1
        ans = 0
        while left <= right:
            if maxLeft <= maxRight:
                maxLeft = max(maxLeft, height[left])
                ans += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                ans += maxRight - height[right]
                right -= 1
        return ans
