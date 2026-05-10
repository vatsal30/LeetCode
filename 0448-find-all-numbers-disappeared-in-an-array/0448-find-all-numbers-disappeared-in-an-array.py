class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return [idx + 1 for idx, num in enumerate(nums) if num > 0]