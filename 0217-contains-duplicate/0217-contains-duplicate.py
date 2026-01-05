class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = {}
        for num in nums:
            if num in checker:
                return True
            else:
                checker[num] = 1
        return False