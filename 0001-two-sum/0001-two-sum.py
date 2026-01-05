class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in checker:
                return [checker[diff], idx]
            else:
                checker[num] = idx
