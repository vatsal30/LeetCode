class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = float("inf")
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]    
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans