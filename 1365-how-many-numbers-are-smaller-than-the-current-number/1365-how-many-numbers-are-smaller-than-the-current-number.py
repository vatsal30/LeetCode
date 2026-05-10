class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        return [bisect_left(ordered, num) for num in nums]