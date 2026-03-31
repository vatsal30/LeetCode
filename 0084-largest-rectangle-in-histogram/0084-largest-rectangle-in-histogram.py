class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i, height in enumerate(heights):
            last_idx = i
            while stack and stack[-1][1] > height:
                last_idx, prev_height = stack.pop()
                ans = max(ans, (i - last_idx) * prev_height)
            stack.append((last_idx, height))
        while stack:
            idx, prev_height = stack.pop()
            ans = max(ans, (i - idx + 1) * prev_height)
        return ans

            