class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] != 0 and zero_idx >= 0:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1
            idx += 1
        return nums
              
