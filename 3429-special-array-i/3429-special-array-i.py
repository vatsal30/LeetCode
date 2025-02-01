class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        for idx in range(1, n):
            if nums[idx-1] % 2 == nums[idx] % 2:
                return False
        return True