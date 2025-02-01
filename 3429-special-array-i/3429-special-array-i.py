class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parityArr = [1 if num % 2 == 0 else 0 for num in nums]
        n = len(nums)
        if n == 1:
            return True
        for idx in range(1, n):
            if parityArr[idx-1] == parityArr[idx]:
                return False
        return True