class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_sum = sum(set(nums))
        dup = sum(nums) - set_sum
        missing = sum(range(1, len(nums) + 1)) - set_sum
        return [dup, missing]