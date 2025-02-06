class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = float("-inf")
        start = 0
        end = len(height) - 1
        while start < end:
            area = (end - start) * min(height[start], height[end])
            ans = max(ans, area)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return ans
        