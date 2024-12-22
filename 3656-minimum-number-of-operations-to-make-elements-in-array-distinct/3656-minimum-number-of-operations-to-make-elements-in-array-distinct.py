class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        while len(num_set) != len(nums):
            nums = nums[3:]
            num_set = set(nums)
            ans += 1
        return ans