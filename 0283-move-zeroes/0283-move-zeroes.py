class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero_idx = 0
        idx = 0
        n = len(nums)
        while nums[nonzero_idx] == 0:
            nonzero_idx += 1
            if nonzero_idx > n - 1:
                return
        while idx < n and nonzero_idx < n: 
            while nonzero_idx < idx or nums[nonzero_idx] == 0:
                nonzero_idx += 1
                if nonzero_idx > n - 1:
                    return
            if nums[idx] == 0:
                nums[idx], nums[nonzero_idx] = nums[nonzero_idx], nums[idx]
                nonzero_idx += 1
            idx += 1
            
