class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = float("-inf")
        currSum = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx-1]:
                currSum += nums[idx]
            else:
                ans = max(ans, currSum)
                currSum = nums[idx]
        return max(ans, currSum)
        