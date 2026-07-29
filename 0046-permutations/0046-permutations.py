class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(perm):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(perm)
                    perm.pop()
        backtrack([])
        return result