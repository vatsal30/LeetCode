
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = []
        for i in range(len(nums)):
            right -= nums[i]
            ans.append(abs(left - right))
            left += nums[i]
        return ans
        