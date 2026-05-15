class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            min_height = min(height[right], height[left])
            width = right - left
            ans = max(ans, min_height * width)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return ans
