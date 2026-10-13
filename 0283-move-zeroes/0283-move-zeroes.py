class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = -1
        idx = 0
        n = len(nums)
        while idx < n:
            if nums[idx] == 0:
                zero_idx = idx
                break
            idx += 1
        idx = zero_idx + 1
        while idx < n:
            if nums[idx] != 0 and zero_idx >= 0:
                nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
                zero_idx += 1
            idx += 1
        return nums
              
