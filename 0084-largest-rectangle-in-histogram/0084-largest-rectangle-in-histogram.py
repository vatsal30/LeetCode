class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for idx, height in enumerate(heights):
            prev = idx
            while stack and stack[-1][0] > height:
                h, prev = stack.pop()
                ans = max(ans, h * (idx - prev))
            stack.append([height, prev])
        
        while stack:
            h, i = stack.pop()
            ans = max(ans, h * (idx - i + 1))
        return ans

        