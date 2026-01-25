class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        ans = 0
        idx = 0
        idx2 = n - 1
        leftMax = height[idx]
        rightMax = height[idx2]
        while idx < idx2:
            if rightMax > leftMax:
                idx += 1
                leftMax = max(leftMax, height[idx])
                ans += leftMax - height[idx]
            else:
                idx2 -= 1
                rightMax = max(rightMax, height[idx2])
                ans += rightMax - height[idx2]
        return ans

                