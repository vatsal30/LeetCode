class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # max_left = [0] * n
        # max_right = [0] * n
        # ans = 0
        # for idx, num in enumerate(height):
        #     if idx == 0:
        #         max_left[idx] = height[idx]
        #         max_right[-1] = height[-1]
        #     elif idx == n-1:
        #         max_right[0] = max(max_right[1], num)
        #         max_left[idx] = max(max_left[idx-1], num) 
        #     else:
        #         max_right[n-idx-1] = max(max_right[n-idx], height[n-idx-1])
        #         max_left[idx] = max(max_left[idx-1], num)
        # for idx in range(1, n-1):
        #     ans += min(max_left[idx], max_right[idx]) - height[idx]
        ans = 0
        left_max = height[0]
        right_max = height[-1]
        start = 0
        end = n - 1
        while start < end:
            if right_max > left_max:
                start += 1
                left_max = max(left_max, height[start])
                ans += (left_max - height[start])
            else:
                end -= 1
                right_max = max(right_max, height[end])
                ans += (right_max - height[end])
        return ans