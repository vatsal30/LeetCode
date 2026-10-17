class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        left = 0
        curr = 0
        haveZeros = 0
        ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > goal:
                curr -= nums[left]
                left += 1
                haveZeros = 0
            if left <= right and curr == goal:
                while left < right and nums[left] == 0:
                    left += 1
                    haveZeros += 1
                ans += haveZeros + 1
        return ans