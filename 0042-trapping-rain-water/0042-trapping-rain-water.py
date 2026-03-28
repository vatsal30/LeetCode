class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) - 1
        leftArr = [0] * (n + 1)
        rightArr = [0] * (n + 1)
        leftArr[0] = height[0]
        rightArr[n] = height[n]
        for i in range(1, n + 1):
            leftArr[i] = max(leftArr[i-1], height[i])
            rightArr[n-i]  = max(rightArr[n-i+1], height[n-i])
        ans = 0
        for i, h in enumerate(height):
            ans += min(leftArr[i], rightArr[i]) - h
        return ans
