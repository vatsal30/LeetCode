class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        noZero = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                noZero += 1
            if noZero > k:
                if nums[left] == 0:
                    noZero -= 1
                left += 1
        return right - left + 1